import torch
import torch.nn as nn
from torch.optim import Adam
from torchvision.utils import save_image

import os

from model import ConvolutionalAE
# from vis_tool import Visualizer

class Trainer(object):
    def __init__(self, train_loader, test_loader, config):
        self.train_loader = train_loader
        self.test_loader = test_loader
        self.config = config
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        self.num_epochs = config.num_epochs
        self.lr = config.lr
        self.weight_decay = config.weight_decay

        self.in_channel = config.in_channel
        self.image_size = config.image_size
        self.hidden_dim = config.hidden_dim
        self.output_dim = config.output_dim

        self.log_interval = config.log_interval
        self.sample_interval = config.sample_interval
        self.ckpt_interval = config.ckpt_interval

        self.sample_folder = config.sample_folder
        self.ckpt_folder = config.ckpt_folder

        self.build_net()
        # self.vis = Visualizer()

    def build_net(self):
        # define network
        self.net = ConvolutionalAE(self.in_channel, self.hidden_dim, self.output_dim)

        if self.config.mode == 'test' and self.config.training_path == '':
            print("[*] Enter model path!")
            exit()

        # if training model exists
        if self.config.training_path != '':
            self.net.load_state_dict(torch.load(self.config.training_path, map_location=lambda storage, loc: storage))
            print("[*] Load weight from {}!".format(self.config.training_path))

        self.net.to(self.device)

    def train(self):
        def denorm(x):
           out = (x + 1) / 2
           return out.clamp(0, 1)
        # define loss function
        mse_criterion = nn.MSELoss().to(self.device)

        # define optimizer
        optimizer = Adam(self.net.parameters(), self.lr, weight_decay=self.weight_decay)

        step = 0
        print("[*] Learning started!")

        for epoch in range(self.num_epochs):
            for i, (imgs, _) in enumerate(self.train_loader):

                self.net.train()
                imgs = imgs.to(self.device)

                # forwarding and compute loss
                outputs = self.net(imgs)
                loss = mse_criterion(outputs, imgs)

                # backwarding
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                # do logging
                if (step+1) % self.log_interval == 0:
                    print("[{}/{}] [{}/{}] Loss:{:3f}".format(
                        epoch+1, self.num_epochs, i+1, len(self.train_loader), loss.item()/len(imgs))
                    )

                # do sampling
                if (step+1) % self.sample_interval == 0:
                    outputs = outputs.view(-1, self.in_channel, self.image_size, self.image_size)
                    x_hat_path = os.path.join(self.sample_folder, 'output_epoch{}.png'.format(epoch+1))
                    save_image(denorm(outputs), x_hat_path)
                    print("[*] Save sample images!")

                step += 1

            if (epoch+1) % self.ckpt_interval == 0:
                ckpt_path = os.path.join(self.ckpt_folder, 'ckpt_epoch{}.pth'.format(epoch+1))
                torch.save(self.net.state_dict(), ckpt_path)
                print("[*] Checkpoint saved!")

        print("[*] Learning finished!")
        ckpt_path = os.path.join(self.ckpt_folder, 'final_model.pth')
        torch.save(self.net.state_dict(), ckpt_path)
        print("[*] Final weight saved!")
