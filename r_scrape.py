import praw
import pandas as pd
import json 
import argparse

def scrape_posts(q, sub, limit, output_dir):

  r = praw.Reddit(client_id='',
  client_secret='',
  password='',
  user_agent='',
  username = '')

  sort="top"
  top_posts = r.subreddit(sub).search(q, sort=sort, limit=limit)
  total_posts = list()

  for post in top_posts:
    Title=post.title,
    Score = post.score,
    Number_Of_Comments = post.num_comments,

    comments = []
    for comment in post.comments:
       try:
         comments.append(comment.body)
       except:
         print("No comment!!")

    Publish_Date = post.created,
    Link = post.permalink,
    data_set = {"Title":Title[0], "Score":Score[0], "Number_Of_Comments":Number_Of_Comments[0], "Comments":comments, "Publish_Date":Publish_Date[0], "Link":'https://www.reddit.com'+Link[0]}
  total_posts.append(data_set)

  df = pd.DataFrame(total_posts)
  df.to_csv(output_dir + '/data.csv', sep=',', index=False)

  json_string = json.dumps(total_posts)
  jsonFile = open(output_dir + "/data.json", "w")
  jsonFile.write(json_string)
  jsonFile.close()


if __name__ == '__main__':
    ap = argparse.ArgumentParser()

    # Adding Arguments
    ap.add_argument("-q", "--query", required=True, type=str, help="query")
    ap.add_argument("-sub", "--subreddit", required=True, type=str, help="subreddit")
    ap.add_argument("-limit", "--limit", required=True, type=int, help="limit")
    ap.add_argument("-output_dir", "--output_dir", required=True, type=str, help='output_dir directory')

    args = vars(ap.parse_args())

    for ii, item in enumerate(args):
        print(item + ': ' + str(args[item]))

    scrape_posts(args['query'], args['subreddit'], args['limit'], args['output_dir'])