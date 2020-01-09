% name = 'Boring_test';
% for i=1:10
%     filename = [name num2str(i) '.csv'];
%     data = importdata(filename);
%     move = data.data(:,1);
%     score = data.data(:,2);
%     plot(move,score, '-.b');
%     xlabel('Move')
% 	ylabel('Score')
% 	title('Boring Agent')
%     axis([0 500 0 36])
%     hold on
% end
 
% name = 'Boring_test';
% for i=11:20
%     filename = [name num2str(i) '.csv'];
%     data = importdata(filename);
%     move = data.data(:,1);
%     score = data.data(:,2);
%     plot(move,score, '-.k');
%     xlabel('Move')
% 	ylabel('Score')
% 	title('Boring Agent')
%     axis([0 50000 0 400])
%     hold on
% end

% name = 'Greedy_test';
% for i=1:10
%     filename = [name num2str(i) '.csv'];
%     data = importdata(filename);
%     move = data.data(:,1);
%     score = data.data(:,2);
%     plot(move,score, '-.k');
%     xlabel('Move')
% 	ylabel('Score')
% 	title('Greedy Agent')
%     axis([0 500 0 36])
%     hold on
% end



% name = 'Greedy_test';
% for i=11:20
%     filename = [name num2str(i) '.csv'];
%     data = importdata(filename);
%     move = data.data(:,1);
%     score = data.data(:,2);
%     plot(move,score, '-.k');
%     xlabel('Move')
% 	ylabel('Score')
% 	title('Greedy Agent')
%     axis([0 1000 0 400])
%     hold on
% end


% name = 'BFS_test';
% for i=1:10
%     filename = [name num2str(i) '.csv'];
%     data = importdata(filename);
%     move = data.data(:,1);
%     score = data.data(:,2);
%     plot(move,score, '-.g');
%     xlabel('Move')
% 	ylabel('Score')
% 	title('BFS Agent')
%     axis([0 500 0 36])
%     hold on
% end

% name = 'Astar_test';
% for i=1:10
%     filename = [name num2str(i) '.csv'];
%     data = importdata(filename);
%     move = data.data(:,1);
%     score = data.data(:,2);
%     plot(move,score, '-.r');
%     xlabel('Move')
% 	ylabel('Score')
% 	title('Astar Agent')
%     axis([0 500 0 36])
%     hold on
% end

% name = 'AstarWithForwardChecking_test';
% for i=1:10
%     filename = [name num2str(i) '.csv'];
%     data = importdata(filename);
%     move = data.data(:,1);
%     score = data.data(:,2);
%     plot(move,score, '-.r');
%     xlabel('Move')
% 	ylabel('Score')
% 	title('Astar with forward checking Agent')
%     axis([0 500 0 36])
%     hold on
% end

% name = 'LongLive_test';
% for i=1:10
%     filename = [name num2str(i) '.csv'];
%     data = importdata(filename);
%     move = data.data(:,1);
%     score = data.data(:,2);
%     plot(move,score, '-.r');
%     xlabel('Move')
% 	ylabel('Score')
% 	title('LongLive Agent')
%     axis([0 10000 0 100])
%     hold on
% end

% name = 'Boring_test';
% for i=21:30
%     filename = [name num2str(i) '.csv'];
%     data = importdata(filename);
%     move = data.data(:,1);
%     score = data.data(:,2);
%     plot(move,score, '-.k');
%     xlabel('Move')
% 	ylabel('Score')
% 	title('Boring Agent')
%     axis([0 10000 0 100])
%     hold on
% end


% name = 'Greedy_test';
% for i=11:20
%     filename = [name num2str(i) '.csv'];
%     data = importdata(filename);
%     move = data.data(:,1);
%     score = data.data(:,2);
%     plot(move,score, '-.k');
%     xlabel('Move')
% 	ylabel('Score')
% 	title('Greedy Agent')
%     axis([0 1000 0 400])
%     hold on
% end

name = 'Greedy_test';
for i=21:30
    filename = [name num2str(i) '.csv'];
    data = importdata(filename);
    move = data.data(:,1);
    score = data.data(:,2);
    plot(move,score, '-.k');
    xlabel('Move')
	ylabel('Score')
	title('Greedy Agent 40x40 Map')
    axis([0 2000 0 100])
    hold on
end

name = 'QL_test';
for i=1:10
    filename = [name num2str(i) '.csv'];
    data = importdata(filename);
    move = data.data(:,1);
    score = data.data(:,2);
    plot(move,score, '-.b');
    xlabel('Move')
	ylabel('Score')
	title('QL Agent 40x40 Map')
    axis([0 2000 0 100])
    hold on
end