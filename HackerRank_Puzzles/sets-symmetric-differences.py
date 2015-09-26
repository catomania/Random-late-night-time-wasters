# https://www.hackerrank.com/challenges/sets (learn about sets!)

# print symmetric (values that are exclusively unique to each set) differences in ascending order 

# turn raw input into sets.



# get inputs from puzzle
m_name = raw_input() 
m_values = raw_input()

n_name = raw_input()
n_values = raw_input()


# convert inputs into sets
m_lis = m_values.split() #split by space

m_lis_new = list(map(int, m_lis)) #convert to list of integers


n_lis = n_values.split() # split by space
n_lis_new = list(map(int, n_lis)) # convert to list of int

# create the sets by inserting in list values - sets are an unordered bag of unique values

m_set = set(m_lis_new)
n_set = set(n_lis_new)

# find values that exist in both M and N:

intersection = list(m_set.intersection(n_set))

# discard intersection values from M and N sets

for x in intersection:
	m_set.discard(int(x))
	n_set.discard(int(x))

# take what's left in m_set and put it in n_set


for x in m_set:
	n_set.add(x)

# put the newly merged n_set into a list (so we can order it)
symmetric_list = list(n_set)

#sort the list
symmetric_list.sort()

for x in symmetric_list:
	print int(x)


