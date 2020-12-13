# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(damages):
  updated_damages = []
  for i in damages:
    if "M" in i and i != "Damages not recorded":
      updated_damages.append(float(i.strip("M"))*1000000)
    elif "B" in i and i != "Damages not recorded":
      updated_damages.append(float(i.strip("B"))*1000000000)
    else:
      updated_damages.append("Damages not recorded")
  return updated_damages
updated_damages = update_damages(damages)

# write your construct hurricane dictionary function here:
def hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  hurricane_dict = {}
  count=0
  for i in names:
    one_hurr = {"Name":i, "Month":months[count],"Year":years[count],"Max Sustained Wind":max_sustained_winds[count],"Areas Affected":areas_affected[count],"Damage":updated_damages[count],"Deaths":deaths[count]}
    hurricane_dict[i]=[one_hurr]
    count+=1
  return hurricane_dict

hurricane_dict = hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

# write your construct hurricane by year dictionary function here:
def hurricane_dict_by_year(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurricane_dict = {}
  count=0
  for i in names:
    one_hurr = {"Name":i, "Month":months[count],"Year":years[count],"Max Sustained Wind":max_sustained_winds[count],"Areas Affected":areas_affected[count],"Damage":updated_damages[count],"Deaths":deaths[count]}
    if hurricane_dict.get(years[count],0)!=0:
      hurricane_dict[years[count]].append(one_hurr)
    else:
      hurricane_dict[years[count]]=[one_hurr]
    count+=1
  return hurricane_dict

# write your count affected areas function here:
def count_affected_areas(areas_affected):
  area_list=[]
  count =[]
  for i in areas_affected:
    for m in i:
      count1=0
      if m not in area_list:
        count1+=1
        area_list.append(m)
        count.append(count1)
      else:
        count[area_list.index(m)]+=1
    count_affected_areas = {x:y for x,y in zip(area_list,count)}
  return count_affected_areas
count_affected_areas_list = count_affected_areas(areas_affected)

# write your find most affected area function here:
def most_affected_area(count_affected_areas_list):
  area_list=[]
  count =[]
  for x,y in count_affected_areas_list.items():
    area_list.append(x)
    count.append(y)
  sorted_count=sorted(count)
  count_max = sorted_count[-1]
  return area_list[count.index(count_max)], count_max

# write your greatest number of deaths function here:
def number_of_deaths(hurricane_dict):
  names = []
  number_of_deaths = []
  for x,y in hurricane_dict.items():
    names.append(x)
    for i in y:
      number_of_deaths.append(i["Deaths"])
  sorted_num_deaths = sorted(number_of_deaths)
  max_deaths_num = sorted_num_deaths[-1]
  return names[number_of_deaths.index(max_deaths_num)],max_deaths_num

# write your catgeorize by mortality function here:
def hurricanes_by_mortality(hurricane_dict):
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for x,y in hurricane_dict.items():
    for i in y:
      if i["Deaths"]>10000:
        hurricanes_by_mortality[5].append(x)
      elif 1000<i["Deaths"]<=10000:
        hurricanes_by_mortality[4].append(x)
      elif 500<i["Deaths"]<=1000:
        hurricanes_by_mortality[3].append(x)
      elif 100<i["Deaths"]<=500:
        hurricanes_by_mortality[2].append(x)
      elif 0<i["Deaths"]<=100:
        hurricanes_by_mortality[1].append(x)
      else:
        hurricanes_by_mortality[0].append(x)
  return hurricanes_by_mortality

# write your greatest damage function here:
def greates_damage(hurricane_dict):
  names =[]
  damages =[]
  for x,y in hurricane_dict.items():
    for i in y:
      if i["Damage"] != 'Damages not recorded':
        names.append(x)
        damages.append(i["Damage"])
  sorted_damages = sorted(damages)
  max_damage = sorted_damages[-1]
  return names[damages.index(max_damage)] ,max_damage

# write your catgeorize by damage function here:
def damage_scale(hurricane_dict):
  damage_scale = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for x,y in hurricane_dict.items():
    for i in y:
      if i["Damage"] == "Damages not recorded":
        damage_scale[0].append(x)
      elif i["Damage"]>50000000000:
        damage_scale[5].append(x)
      elif 10000000000<i["Damage"]<=50000000000:
        damage_scale[4].append(x)
      elif 1000000000<i["Damage"]<=10000000000:
        damage_scale[3].append(x)
      elif 100000000<i["Damage"]<=1000000000:
        damage_scale[2].append(x)
      elif 0<i["Damage"]<=100000000:
        damage_scale[1].append(x)

  return damage_scale