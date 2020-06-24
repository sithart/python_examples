highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')

print(highlighted_poems_list)

highlighted_poems_stripped = []

for elt in highlighted_poems_list:
  highlighted_poems_stripped.append(elt.strip())

print(highlighted_poems_stripped)

highlighted_poems_details = []

for elt_data in highlighted_poems_stripped:
  highlighted_poems_details.append(elt_data.split(':'))
print(highlighted_poems_details)

titles = []
poets = []
dates = []

for elt2 in highlighted_poems_details:
  titles.append(elt2[0])
  poets.append(elt2[1])
  dates.append(elt2[2])

print(titles)
print(poets)
print(dates)

counter = 0
for i in range(len(titles)):
  print("The poem {} was published by {} in {}".format(titles[i],poets[i],dates[i]))
