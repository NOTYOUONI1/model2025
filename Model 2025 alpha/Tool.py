from scipy.spatial.distance import hamming
import numpy as np

# Define the function to find the closest label
def find_closest_label(input_label):
    dataset = [
    "AAPL",  # Apple Inc.
    "MSFT",  # Microsoft Corporation
    "AMZN",  # Amazon.com, Inc.
    "GOOGL",  # Alphabet Inc. (Google)
    "TSLA",  # Tesla, Inc.
    "FB",  # Meta Platforms, Inc. (Facebook)
    "NFLX",  # Netflix, Inc.
    "NVDA",  # NVIDIA Corporation
    "JNJ",  # Johnson & Johnson
    "V",  # Visa Inc.
    "AAPE",  # Almost identical to "AAPL"
    "^GSPC",  # S&P 500 Index
    "^DJI",  # Dow Jones Industrial Average
    "^IXIC",  # NASDAQ Composite Index
    "^RUT",  # Russell 2000 Index
    "^VIX",  # CBOE Volatility Index
    "BABA",  # Alibaba Group Holding Limited (China)
    "TSM",  # Taiwan Semiconductor Manufacturing Company (Taiwan)
    "RDS.A",  # Royal Dutch Shell plc (UK)
    "TM",  # Toyota Motor Corporation (Japan)
    "NIO",  # NIO Inc. (China)
    "BTC-USD",  # Bitcoin (USD)
    "ETH-USD",  # Ethereum (USD)
    "DOGE-USD",  # Dogecoin (USD)
    "ADA-USD",  # Cardano (USD)
    "BNB-USD"  # Binance Coin (USD)
    ]

    def to_binary_vector(label, length):
        return [int(bin(ord(char)).replace('0b', '').zfill(8)) for char in label.ljust(length)]
    
    # Encode all labels
    max_length = max(len(l) for l in dataset + [input_label])  # Find the maximum label length
    binary_labels = np.array([to_binary_vector(l, max_length) for l in dataset])
    
    # Encode the input label
    input_binary_vector = to_binary_vector(input_label, max_length)
    
    # Calculate Hamming distances
    min_distance = float('inf')
    closest_label = None
    
    for i in range(len(dataset)):
        distance = hamming(input_binary_vector, binary_labels[i]) * max_length
        if distance < min_distance:
            min_distance = distance
            closest_label = dataset[i]
    
    return closest_label


def tty_color(text, color):
    """
    Apply color to the terminal text.

    :param text: The text to be colored.
    :param color: The color code for the text.
                   Examples of color codes:
                   30 = Black
                   31 = Red
                   32 = Green
                   33 = Yellow
                   34 = Blue
                   35 = Magenta
                   36 = Cyan
                   37 = White
    :return: The colored text.
    """
    # ANSI escape code for text color
    return f"\033[38;5;{color}m{text}\033[0m"