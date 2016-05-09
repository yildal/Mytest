df['city_id'].value_counts()
cityCount = df['city_id'].value_counts()
p.bar(range(30), cityCount[:30])
p.show()

tst = df[df['clicks'] == df['clicks'].isnull()]

tst = df[df['clicks'].isnull() == False]

is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
noise_complaints = complaints[is_noise]
noise_complaints['Borough'].value_counts()


