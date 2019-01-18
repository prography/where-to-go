import torch.nn as nn

class ConvolutionalAE(nn.Module):
    def __init__(self, in_channel, hidden_dim, output_dim):
        super(ConvolutionalAE, self).__init__()
        self.in_channel = in_channel
        self.hidden_dim = 400
        self.hidden_dim2 = 200
        self.hidden_dim3 = 100
        self.output_dim = 50

        # encoder network
        self.encoder = nn.Sequential(
            nn.Conv2d(self.in_channel, self.hidden_dim, kernel_size=4, stride=4, padding=0),
            nn.ReLU(True),
            nn.Conv2d(self.hidden_dim, self.hidden_dim2, kernel_size=4, stride=4, padding=0),
            nn.ReLU(True),
            nn.Conv2d(self.hidden_dim2, self.hidden_dim3, kernel_size=4, stride=4, padding=0),
            nn.ReLU(True),
            nn.Conv2d(self.hidden_dim3, self.output_dim, kernel_size=4, stride=4, padding=0),
            nn.ReLU(True),
        )

        # decoder network
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(self.output_dim, self.hidden_dim3, kernel_size=4, stride=4, padding=0),
            nn.ReLU(True),
            nn.ConvTranspose2d(self.hidden_dim3, self.hidden_dim2, kernel_size=4, stride=4, padding=0),
            nn.ReLU(True),
            nn.ConvTranspose2d(self.hidden_dim2, self.hidden_dim, kernel_size=4, stride=4, padding=0),
            nn.ReLU(True),
            nn.ConvTranspose2d(self.hidden_dim, self.in_channel, kernel_size=4, stride=4, padding=0),
            nn.Tanh()
        )

    def forward(self, x):
        encoder_out = self.encoder(x)
        decoder_out = self.decoder(encoder_out)
        return decoder_out
