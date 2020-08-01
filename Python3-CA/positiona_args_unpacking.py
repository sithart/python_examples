from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!

all_three = join(path_segment_1,path_segment_2,path_segment_3)

print(all_three)


def myjoin(*args):
  return join(*args)

print(myjoin(path_segment_1,path_segment_2,path_segment_3))
