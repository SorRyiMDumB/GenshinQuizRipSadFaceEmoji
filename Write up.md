# Algorithmics: Write Up
###### Yaseen Ahmad
---
## Summary

I created graph ADT to showcase relationships within the school community and run algorithims detrmining various conclusions. Addtionally, a database was created to manage the raw data. The graph ADT contains multiple smaller ADTs in order to function correctly. 

## Nodes

Nodes have been given several attrivbutes to showcase their data 
### Operational Attributes
#### Year
The `year` attribute was given to nodes to depending on what year level the student is in. This was to show potential diffences in activities between year levels. 

#### House
The `house` attribute was given to nodes to depending on what house the student is in. This was to show potential diffences between the people who know each other. 

#### Classes
The `classes` attribute was given to nodes to depending how many classes they have in common with others. This was also to show people who may know eachother

#### Genshin
The `genshin` attribute was given to nodes to depending on whether they play genshin or not.  This was to show 

#### Uni
The `year` attribute was given to nodes to depending on what year level the student is in. This was to show potential diffences between year levels. 

#### Course
The `year` attribute was given to nodes to depending on what year level the student is in. This was to show potential diffences between year levels. 

#### F1
The `year` attribute was given to nodes to depending on what year level the student is in. This was to show potential diffences between year levels. 

#### Sport
The `year` attribute was given to nodes to depending on what year level the student is in. This was to show potential diffences between year levels. 

#### TutorMath/Eng/Hums/Science
The `year` attribute was given to nodes to depending on what year level the student is in. This was to show potential diffences between year levels. 

#### Friends
The `year` attribute was given to nodes to depending on what year level the student is in. This was to show potential diffences between year levels. 

### Aesthetics
#### Color
The nodes have been given diffrent colours based on multiple factors, such as house, sport or whether they watch Formula 1. 
> This can be shown with the house_node() function which modifies the colour artibute 

#### Size
#### Shape
#### Edge colours


I have avoided using the nodes’ colour attribute (course selection) to group them together in a group of three for the car ride as it only makes the journey longer and increases complexity, which makes the algorithm ineffective. This is because doing this would require a brute force approach with another block and that makes Edgy crash easily. Since Edgy runs with less disruptions with a greedy algorithm approach, I have resorted to using distance and people to be avoided to group them together for the grouping and route, as well as personal necessities such as diet and health problems. For example, I’ve set the label of edge of people who wish to avoid each other to infinity so my algorithm does not pick up them in the same car.

pseudocode:
//i’ll explain my code/choices like this
set var.vnode to "raida"
//raida is the start node
create stack "s"
set var.count.foodjoint to 0
//counts the number of restaurants visited
set var.count.people to 0
//counts the number of people in the car
set var.count.hospital to 0
//counts the number of hospitals visited as it can’t exceed more than one
set var.people to nodes with scale equal to 1.2
set var.food joint to <nodes with food joint equal to true>
create list "picked up"
//list of people in the car + restuarants/ medical centres visited
create list "veglist"
create list "foodlist"
create list "peoplelist"
set "peoplelist" to <nodes with scale equal to 1.2>
set "foodlist" to <nodes with food joint equal to true>
set "hospital" to <nodes with colour equal to blue>
repeat until <vnode = "melbourne">
	for each neighbour of neighbours of vnode 
		if <not <picked up contains neighbour>>
			push neighbour to stack s
		set temp to <(distance of node vnode) + (label of edge <edge (vnode, neighbour)>)>
		if temp < distance of node neighbour
			set distance of node neighbour to temp
//so values of distance don’t get overlapped/ added again and again
	set stack.s to <nodes s sorted by distance ascending>
//Dijkstra’s algorithm to find the shortest path to the next node. It’s basically breadth first search with a greedy algorithm incorporated.
	set veglist to <nodes (nodes with colour equal to green) sorted by distance ascending>s
	set foodlist to <nodes foodlist sorted by distance ascending>
	set peoplelist to <nodes peoplelist sorted by distance ascending>
	set hospital to <nodes hospital sorted by distance ascending>
//arranged in ascending order for distance so the top of these lists is the closest to vnode. contributes to Dijkjstra 
	if nodes with health complications equal to true contains vnode
		set vnode to <item 1 of hospital>
		add vnode to picked up
//so that people with health complications have a hospital on the way
	if count.people = 3
		if count.foodjoint < 1
			if <nodes with vegetarian equal to true> contains vnode>
				set vnode to <item 1 of veglist>
				add vnode to picked up
				for each item of picked up
					if <foodlist contains item>
						set count.foodjoint to count.foodjoint + 1
				delete 1 of foodlist
//when car is at full capacity with three people and a restaurant hasn’t been visited yet and there’s a vegetarian person in the car, we will pass the closest vegetarian restaurant from the third person picked up. Food joint count will be at 1. 
			else
				set vnode to item 1 of foodlist 
				add vnode to picked up
				for each item of picked up
					if <foodlist contains item>
						set count.foodjoint to count.foodjoint + 1
				delete 1 of foodlist
//when the car is at full capacity with three people and a restaurant hasn’t been visited yet, we will pass the closest restaurant from the third person picked up. Food joint count will be at 1 and deletes from peoplelist so the numbers don’t overlap.
		else
			if count.foodjoint = 1
				set vnode to melbourne
				add vnode to picked up
//when the food joint is visited, university will be next on the list as we’ve been to all three people and a restaurant. 
	else
		if count.people < 3
			set vnode to item 1 of peoplelist
			add vnode to picked up
			for each item of picked up
				if <peoplelist contains item>
					set count.people to count.people + 1
			delete 1 of peoplelist
//while the car isn’t full, pick up three people. People.count counts until it is 3 and deletes from peoplelist so the numbers don’t overlap. 
set distance to <distance of node melbourne>
//add up of labels of edges from start node

Detailed explanation of pseudocode:
Overall, the closest specified location from vnode is calculated. For example, if vnode is Raida and the car, which is named variable “picked up” is empty, the algorithm will individually add the distance of the vnode to each possible pathway’s label and set the distance of its neighbours to that number. The closest neighbour will be set as vnode, which in this case is Marcus. The count for people will be set to 1 from 0. Now that Marcus is vnode and the car has one person, the algorithm will look for more closest people-vnodes until the car has 3 people/ until the count for people equals 3. From vnode-Marcus, the distance of Marcus from the start plus label of closest edge will be added to obtain a new closest neighbour, Malachi. Distances of each vnode are added and renewed so each label of the pathway is added because the full distance to Melbourne University from the start can be calculated. Now, the count of people is 2, so closest people-neighbour Alexandria becomes vnode. 

Since count is now 3, the algorithm will look for a food joint, and if “picked up”, which is the vnodes visited, contains a node with node attribute vegetarian, a vegetarian food joint with node attribute “veg” will be chosen. If a person with health complications is the vnode, then the next vnode will be the closest medical centre to incorporate a medical centre in their route. After the food joint is visited, the university must be the next vnode. This would make sense in a real world situation as you would eat after you collect everyone and during the long part of the journey, since no matter how far the university is, we would have to travel from the food joint. 

For unavoidable reasons, food joints and Melbourne Uni are added to “picked up”. I tried making new variables to store the food joint and university but edgy ended up crashing every time I did. I think I exceeded the maximum number of variables, or because edgy doesn’t have the caliber to display multiple variables at once. Either way, it isn’t a big issue.
