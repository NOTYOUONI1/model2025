import matplotlib.pyplot as plt
import numpy as np

# উদাহরণস্বরূপ ডেটা
prices = [100, 102, 105, 104, 107, 106, 108, 107, 109, 110]
dates = list(range(len(prices)))

# সহায়ক ফাংশন: দাম স্পর্শের স্তর খুঁজে বের করা (0.1% থ্রেশহোল্ড ব্যবহার করে)
def find_levels(prices, threshold_percentage=0.1, min_touches=3):
    levels = []
    price_array = np.array(prices)
    
    for i in range(len(prices)):
        level = prices[i]
        threshold = level * threshold_percentage / 100
        
        # নিকটতম দামের সংখ্যা গণনা করা
        count = np.sum((price_array >= level - threshold) & (price_array <= level + threshold))
        
        if count >= min_touches and level not in levels:
            levels.append(level)
    
    return levels

# স্তরের জন্য হরিজন্টাল লাইন আঁকতে বের করুন
support_resistance_levels = find_levels(prices, threshold_percentage=0.1, min_touches=3)

# লাইন ড্র করা
plt.plot(dates, prices, marker='o', linestyle='-', color='b')

# দাম আশেপাশে হরিজন্টাল লাইন আঁকতে
for level in support_resistance_levels:
    plt.axhline(y=level, color='r', linestyle='--')

plt.xlabel('দিন')
plt.ylabel('দাম')
plt.title('মার্কেট মুভমেন্ট')
plt.grid(True)
plt.show()
