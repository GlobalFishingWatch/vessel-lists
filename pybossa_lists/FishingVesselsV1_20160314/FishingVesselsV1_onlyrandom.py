import csv

fieldnames = ['mmsi','link','users','responses','longliner','pursseiner','trawler','reefers','multigear','other fishing','notfishing','multiple','baddata','not known','other','othertext','websitesfound']
new_rows  = []
clav_rows = []
mmsi_random = [412002777,316008961,412423199,412328565,440000690,412418996,412430414,251194540,200000055,227101600,412479576,412061922,110701275,412432048,247155210,412437435,257488620,412448749,416004801,412444188,224055250,412447295,412464376,412462593,800017081,412444796,412286699,413011032,432845000,412412715,219019804,412421803,412449545,412416335,231184000,701000662,725009500,412360539,900658520,412441214,257705500,900405802,247051730,257001210,412596013,412450746,412123411,265502370,251415640,800028837,412428092,900303106,412411689,263583000,90143213,413441090,261008070,235071779,412433799,224094160,271072382,412457011,247121880,412433643,228282000,265616100,247121820,412464495,338145405,412515898,235087027,412464331,410025515,412489777,412441905,412445383,412449247,412323921,412417063,412478686,412450085,304145000,247143580,900402635,270007565,412435094,265668860,130400923,412329271,272740000,412462038,231045000,412064497,412431119,412416059,412201603,412413956,412286805,251576540,900019534,412421998,412430411,412418804,224020790,412422289,412698540,412300862,259595000,413214763,900412851,412469752,412460866,412427022,431702990,412330746,412418459,235090864,900264110,412418411,228258000,412412192,271062117,412202537,412568997,800036705,367416270,412413602,412418986,412423422,247063630,412213273,699889966,251080110,210000009,205155000,412328001]


with open('FishingVesselsV1_20160314.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if int(row['mmsi']) in mmsi_random:
            new_rows.append(row)
        else:
            clav_rows.append(row)


with open('FishingVesselsV1_20160314_random.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_rows)


with open('FishingVesselsV1_20160314_clav.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(clav_rows)



new_rows  = []
clav_rows = []
fieldnames = ['mmsi','student_label','student_confidence','pybossa_url']
with open('../FishingVesselsV1_20160314_agreement.csv','rU') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if int(row['mmsi']) in mmsi_random:
            new_rows.append(row)
        else:
            clav_rows.append(row)  


with open('FishingVesselsV1_20160314_agreement_random.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_rows)


with open('FishingVesselsV1_20160314_agreement_clav.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(clav_rows)