import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("zomato dataset.csv",encoding='latin1')
pd.set_option("display.max_columns",None)
pd.set_option("display.max_colwidth",None)
pd.set_option("display.width",None)
print(df)

print()
print()

#DELETE A COLUMN
df = df.drop(columns=["Locality Verbose"])
print(df)

print(df.isnull().sum())

print(df.info())

a = df[df["Cuisines"].isnull()]
print(a)

print()

df["Cuisines"] = df["Cuisines"].fillna("unknown")
print(df)

print(df.isnull().sum())

print()
#SHOW FIRST 500 ROWS
# pd.set_option("display.max_rows",500)
# print(df.head(500))

print(df.describe())

print(df.duplicated().sum())

print(df.duplicated("Restaurant ID").sum())

print(df["Restaurant Name"].unique())

df.drop_duplicates(inplace=True)
print(df)

#1.TOP 10 CITIES BY NUMBER OF RESTAURANTS
top_city = df["City"].value_counts().head(10)
print(top_city)

print()

#2.MOST POPULAR CUISINE
cuisine = df["Cuisines"].value_counts().head(10)
print(cuisine)

print()

#3.AVG RATING BY CITY
rating = df.groupby("City")["Aggregate rating"].mean().sort_values(ascending=False).head(10)
print(rating)

print()

#4.AVG COST FOR TWO BY CITY
city = df.groupby("City")["Average Cost for two"].mean().sort_values(ascending=False).head(10)
print("AVG_COST_FOR_TWO")
print(city)

print()

#5.ONLINE DELIVERY VS RATING
delivery = df.groupby("Has Online delivery")["Aggregate rating"].mean()
print("ONLINE DELIVERY VS RATING")
print(delivery)

print()

df.to_csv("zoomato.cvs",index=False,encoding="utf-8-sig")
print(df)



top_city = df["City"].value_counts().head(10)
plt.bar(top_city.index,top_city.values,color='#E23744')
plt.title("Top 10 Cities BY NUMBER OF RESTAURANT")
plt.xlabel('City',fontsize=8)
plt.ylabel("RESTAURANT COUNT")
plt.xticks(rotation=50)
plt.tight_layout()

plt.show()

cuisine = df["Cuisines"].value_counts().head(10)
plt.barh(cuisine.index,cuisine.values,color="#E23744",label="TOP 10 CUISINE")
plt.title("Top 10 Cities")
plt.xlabel("RESTAURANT COUNT",fontsize=12,fontweight="bold")
plt.ylabel('CUISINE',fontsize=12,fontweight="bold")
plt.xticks(rotation=50)
plt.tight_layout()

plt.show()

rating = df.groupby("City")["Aggregate rating"].mean().sort_values(ascending=False).head(10)
plt.plot(rating.index,rating.values,color='#E23744',marker='o',label="AVG RATING BY CITY")
plt.title("AVG RATING BY CITY",color="#E23744",fontsize=12,fontweight="bold")
plt.xlabel("city",fontsize=12,fontweight="bold")
plt.ylabel("AVG RATING",fontsize=12,fontweight="bold")
plt.tight_layout()

plt.show()


city = df.groupby("City")["Average Cost for two"].mean().sort_values(ascending=False).head(10)
plt.bar(city.index,city.values,color='#E23744')
plt.title("AVG COST FOIR TWO0")
plt.xlabel("city",fontsize=12,fontweight="bold")
plt.ylabel("AVG COST FOR TWO0",fontsize=12,fontweight="bold")
plt.grid(True)
plt.tight_layout()

plt.show()

delivery = df.groupby("Has Online delivery")["Aggregate rating"].mean()
plt.pie(delivery.values,labels=delivery.index,colors = ['#E23744', '#FFD700'],autopct="%1.1f%%",)
plt.title("AVG COST FOR TWO",fontsize=12,fontweight="bold")
plt.tight_layout()

plt.show()


#SUBPLOT

#plot1
plt.figure(figsize=(18,10))
plt.subplot(3,2,1)
plt.bar(top_city.index,top_city.values,color='#E23744')
plt.title("Top 10 Cities BY NUMBER OF RESTAURANT")
plt.xlabel('City',fontsize=8,fontweight="bold")
plt.ylabel("RESTAURANT COUNT")
plt.xticks(rotation=50)

#plot2
plt.subplot(3,2,2)
plt.barh(cuisine.index,cuisine.values,color="#E23744",label="TOP 10 CUISINE")
plt.title("Top 10 Cities")
plt.xlabel("RESTAURANT COUNT",fontsize=8,fontweight="bold")
plt.ylabel('CUISINE',fontsize=8,fontweight="bold")
plt.xticks(rotation=50)

#plot3
plt.subplot(3,2,3)
plt.plot(rating.index,rating.values,color='#E23744',marker='o',label="AVG RATING BY CITY")
plt.title("AVG RATING BY CITY",color="#E23744",fontsize=8,fontweight="bold")
plt.xlabel("city",fontsize=8,fontweight="bold")
plt.ylabel("AVG RATING",fontsize=8,fontweight="bold")
plt.xticks(rotation=50)

#plot4
plt.subplot(3,2,4)
plt.pie(delivery.values,labels=delivery.index,colors = ['#E23744', '#FFD700'],autopct="%1.1f%%",)
plt.title("ONLINE DELIVERY VS RATING",fontsize=12,fontweight="bold")


#plot5
plt.subplot(3,2,5)
plt.bar(city.index,city.values,color='#E23744')
plt.title("AVG COST FOIR TWO0")
plt.xlabel("city",fontsize=8,fontweight="bold")
plt.ylabel("AVG COST FOR TWO0",fontsize=10,fontweight="bold")
plt.xticks(rotation=50)
plt.grid(True)



plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.suptitle("ZOMATO SALES ANALYSIS",fontsize=14,fontweight="bold",color="#E23744")

plt.savefig("zomato_sales.png",bbox_inches='tight',dpi=300)

plt.show()


print(df.duplicated("Restaurant Name").sum())

df.drop_duplicates(subset="Restaurant Name", inplace=True)
print(df)

top = df["City"].value_counts().head(10)
print(top)

print(df.shape)

print(df.describe())

print()


correlation = df.corr(numeric_only=True)
print(correlation)
