from scraper import save_scores, read_scores

a=read_scores("scores.txt");


array = [0,0,0,0,0];
counter = 0;
num = 0;

for i in a[0]:
    array[i] += 1;
    counter += 1;
for i in a[1]:
    array[i] += 1;
    counter += 1;

for j in array:
    print("%s appears %s times (%.2f%% of all numbers)"%(num, j, 100*j/counter))
    num += 1;
    
