data = importdata('test1.csv');
move = data.data(:,1);
score = data.data(:,2);
plot(move,score);