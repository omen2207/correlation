import csv
import math

def read_csv(file_path):
    x = []
    y = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            x.append(float(row[0])) 
            y.append(float(row[1]))  
    return x, y

def pearson_correlation(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_sq = sum([i**2 for i in x])
    sum_y_sq = sum([i**2 for i in y])
    sum_xy = sum([x[i] * y[i] for i in range(n)])
    
    numerator = sum_xy - (sum_x * sum_y / n)
    denominator = math.sqrt((sum_x_sq - sum_x**2 / n) * (sum_y_sq - sum_y**2 / n))
    
    if denominator == 0:
        return 0
    return numerator / denominator

csv_file = r'C:\Users\bhilw\OneDrive\Documents\DM\iris.csv'
x, y = read_csv(csv_file)

correlation = pearson_correlation(x, y)
print(f"Pearson Correlation: {correlation}")
