
import plotly.express as px
import pandas as pd
import streamlit as st
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="sales dashboard ",
                   page_icon=":bar_chart:",
                   layout="wide"
)                 

df=pd.read_csv("data.csv")




# sns.distplot(np.log(df['Price']))
# plt.show()

# df=pd.read_excel(io='new.xlsx',
#     sheet_name='Sheet1',
#     engine='openpyxl',
#     skiprows=3,
#     usecols='A:N',
#     nrows=1302,
# )

# st.dataframe(df)

st.sidebar.header("please filter Here:")
company=st.sidebar.multiselect(
     "select the Company",
    options=df["Company"].unique(),
    default=df["Company"].unique()
)


typeName=st.sidebar.multiselect(
     "select the TypeName",
    options=df["TypeName"].unique(),
    default=df["TypeName"].unique()
)


ram=st.sidebar.multiselect(
     "select the Ram",
    options=df["Ram"].unique(),
    default=df["Ram"].unique()
)




df_selection =df.query(        
       "Company == @company & TypeName == @typeName & Ram == @ram"
)


# st.dataframe(df_selection)




st.title(":bar_chart:laptop prices dashboard ")
st.markdown("##")

total_sales = int(df_selection["Price"].sum())
average_Weight =round(df_selection["Weight"].mean(),1)
star_Weight = ":star:"* int(round(average_Weight, 0))
average_sale_by_transaction = round(df_selection["Price"].mean(),2)

left_column, middle_column ,right_column =st.columns(3)
with left_column:
    st.subheader("Totel sales:")
    st.subheader(f"US $ {total_sales:,}")     
with middle_column:
    st.subheader("Average Weight:")
    st.subheader(f"{average_Weight} {star_Weight}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sale_by_transaction}") 
                        
st.markdown("---")





# this stap is drow Cpu_brand with price

sales_by_Cpu_brand_line= (
    df_selection.groupby(by=["Cpu_brand"]).sum()[["Price"]].sort_values(by="Price")


)


fig_cpu_brand_price=px.bar(
    
    sales_by_Cpu_brand_line,
    x="Price",
    y=sales_by_Cpu_brand_line.index,
    orientation="h",
    title="<B>prices by brand line</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_Cpu_brand_line),
    template="plotly_white",

)
fig_cpu_brand_price.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))


)


# st.plotly_chart(fig_cpu_brand_price)


# this stap is company with price

sales_company_line= (
    df_selection.groupby(by=["Company"]).sum()[["Price"]]


)


fig_company_price=px.bar(
    
    sales_company_line,
    x="Price",
    y=sales_company_line.index,
    orientation="h",
    title="<B>prices by company line</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_company_line),
    template="plotly_white",

)
fig_company_price.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False))


)

left_column,right_column=st.columns(2)
left_column.plotly_chart(fig_company_price,use_container_width=True)
right_column.plotly_chart(fig_cpu_brand_price,use_container_width=True)


# hide_streamlit style

hide_st_style = """
         <style>
         #MainMenu {visibility: hidden,}
         foorter {visibility: hidden,}
         header {visibility: hidden,}
         </style>
         """
st.markdown(hide_st_style,unsafe_allow_html=True)


