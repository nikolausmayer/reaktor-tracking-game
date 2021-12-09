
import json

data = json.loads(open('003-flood.txt').read())
#data = json.loads(open('003-flood-test.txt').read())

region_letters = []

for region in data['regions']:
    region_name = region['regionID']
    #print("Region", region_name)

    previous_pool_cells = None
    for day in region['readings']:
        readingID = day['readingID']
        dataline  = day['reading']
        date      = day['date']
        #print("Day", date)

        from_left  = [dataline[0]]
        for v in dataline[1:]:
            from_left.append(max(from_left[-1], v))
        from_right = [dataline[-1]]
        for v in dataline[-2::-1]:
            from_right.append(max(from_right[-1], v))
        from_right = from_right[::-1]

        pooled = [(min(l,r) - scan) for scan,l,r in zip(dataline,from_left,from_right)]
        pool_cells = sum(pooled)

        if previous_pool_cells is not None \
           and (pool_cells - previous_pool_cells) > 1000:
            region_letters.append(readingID)
        previous_pool_cells = pool_cells

print(''.join(region_letters))



