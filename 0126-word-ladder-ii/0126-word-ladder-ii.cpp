class Solution {
public:
    vector<vector<string>> ans;
    unordered_map<string, vector<string>> parent;

    void dfs(string word, string beginWord, vector<string>& path) {

        if (word == beginWord) {
            vector<string> temp = path;
            reverse(temp.begin(), temp.end());
            ans.push_back(temp);
            return;
        }

        for (string &p : parent[word]) {
            path.push_back(p);
            dfs(p, beginWord, path);
            path.pop_back();
        }
    }

    vector<vector<string>> findLadders(string beginWord,
                                       string endWord,
                                       vector<string>& wordList) {

        unordered_set<string> dict(wordList.begin(), wordList.end());

        if (!dict.count(endWord))
            return {};

        unordered_map<string,int> dist;

        queue<string> q;
        q.push(beginWord);
        dist[beginWord]=0;

        while(!q.empty()){

            string word=q.front();
            q.pop();

            int d=dist[word];

            string temp=word;

            for(int i=0;i<temp.size();i++){

                char old=temp[i];

                for(char c='a';c<='z';c++){

                    temp[i]=c;

                    if(!dict.count(temp))
                        continue;

                    if(!dist.count(temp)){

                        dist[temp]=d+1;
                        parent[temp].push_back(word);
                        q.push(temp);

                    }else if(dist[temp]==d+1){

                        parent[temp].push_back(word);
                    }
                }

                temp[i]=old;
            }
        }

        if(!dist.count(endWord))
            return {};

        vector<string> path;

        path.push_back(endWord);

        dfs(endWord,beginWord,path);

        return ans;
    }
};