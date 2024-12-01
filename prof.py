import streamlit as st
from streamlit_timeline import timeline
from streamlit_lottie import st_lottie
import requests
import base64
import streamlit.components.v1 as components
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title="Profile", page_icon=":human:", layout="wide")
from streamlit_option_menu import option_menu
# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Menu",["About Me", "Experience","Data Products","Gen AI Products","Education"],
                                   #"Resume","Contact Me"'download',"envelope",""Projects","Domain"],
        icons=['person','compass','laptop','map','circle','cpu','book'], menu_icon="cast", default_index=0)
#tab1, tab2, tab3 = st.tabs(["Timeline", "Skills","Contact Me"])
#st.set_page_config(layout="wide")

# items = [
#     {"id": 1, "content": "2022-10-20", "start": "2022-10-20"},
#     {"id": 2, "content": "2022-10-09", "start": "2022-10-09"},
#     {"id": 3, "content": "2022-10-18", "start": "2022-10-18"},
#     {"id": 4, "content": "2022-10-16", "start": "2022-10-16"},
#     {"id": 5, "content": "2022-10-25", "start": "2022-10-25"},
#     {"id": 6, "content": "2022-10-27", "start": "2022-10-27"},
# ]

# timeline = timeline(items,height=300)
# st.subheader("Selected item")
# st.write(timeline)
#with st.container():
def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
def local_css(file_name):
            with open(file_name) as f:
                 st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()
# lottie_gif = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
# python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
# java_lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
# my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
# git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
# github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
# docker_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
# figma_lottie = load_lottieurl("https://lottie.host/5b6292ef-a82f-4367-a66a-2f130beb5ee8/03Xm3bsVnM.json")
# js_lottie = load_lottieurl("https://lottie.host/fc1ad1cd-012a-4da2-8a11-0f00da670fb9/GqPujskDlr.json")
if selected=='About Me':
    #st.title(":blue[Brief Profile]")
    st.subheader(":blue[Brief Profile]")
    #st.write(":blue[Brief Profile]")
    st.write("⚒️  Techno-functional professional  with **11 years** of experience across various data functions, including Data Analytics and Visualization,Data Products,Data Strategy & Governance in multiple roles such as Data Product Manager/Owner, Lead Consultant, Data Scientist and Engagement Manager.")
    st.write("⚒️  Currently working with **Cognizant Consulting** in **Aritifical Intelligence & Analytics** business unit providing advisory services on Generative AI, Data Strategy, Data Product/Platform Development.")
# • Holds a Management Degree from the Indian Institute of Management (IIM), Kashipur, with a special focus on Systems & Analytics and Marketing. 
# • Proficient in eliciting, gathering and analyzing business requirements, client handling, market research, team management, and stakeholder management. 
# • Experienced in domains such as FMCG, Retail, Insurance and Pharmaceutical. 
# • Skilled in analytics and visualization tools including Python, SQL, Excel, and Power BI. Holds certifications in AZ900 (Data Fundamentals Microsoft), AI900 (AI Fundamentals Microsoft), and PL-300 (Data Analyst- Power BI Microsoft). Proficient in using EIS (Insurance tool).
# • Well-versed in agile & water –fall methodologies. Proficient in project management tools such as Jira, Trello and Confluence.
# ")
    st.divider()
    # st.subheader(':blue[Timeline]')
    # # load data
    # with open(r'C:\Users\DINGOO KARTHICK\Documents\portfolio-template-main\e.json', "r") as f:
    #     data = f.read()

    # # render timeline
    # timeline(data, height=400)
    # st.divider()
    st.subheader(':blue[Voluteering & Personal Projects]')
    st.write("⚒️  Worked as a Digital Marketing Consultant for a Start-Up through the United Nations Development Program, optimizing SEO of the website to drive traffic.")
    st.write("⚒️  Taught a course on Analytics for Management Students of a leading B-school in Chennai.")
    st.divider()
    st.subheader(':blue[Hobbies]')
    st.write("⚒️  Reading books on management, life. Favourite Author: Paulo Coelho. Favourite Book: The Pilgrimage.")
    st.write("⚒️  Playing cricket,football,tennis.Favourite Sport: Cricket ")
    st.divider()
    #st.subheader(':blue[Resu]')
   #  with open(r"C:\Users\DINGOO KARTHICK\Desktop\T\Rsume\L1\Dingoo Karthick G.pdf", "rb") as file:
   #          btn = st.download_button(
   #          label=":blue[Download Resume]",
   #          data=file,
   #          file_name="dingoo.pdf",
   #          mime="pdf"
   #        )
# ----------------- skillset ----------------- #
if selected=='Experience':
   st.subheader(':blue[Experience-Post MBA]')
   st.write("**Cognizant Consulting - Senior Consultant- Jun 2021 to Till Date**")
   #st.write("Project 1- Leading Insurance Company")
   st.write('*Responsibilities:*')
   st.caption("⚒️  Providing strategic roadmap & tactical assistance to senior directors and AVP, helping them to shape key initiatives for fuelling organizational growth.")
   st.caption("⚒️  Day to day activities involves requirement gathering, converting the technical requirement into business requirement. Addressing concerns/questions on the data platform from stakeholders. Showing the demo of the newly introduced features.")
   st.caption("⚒️  Aiding internal sales teamon responding to RFI/RFP by understanding the business & industry landscape and providing relevant frameworks,case studies to build a more concrete proposal.")
   st.caption("⚒️  Supporting Recruitment drives to hire right set of candidates for the organization.")
   st.divider()
   st.write("**LatentView Analytics - Assistant Manager- April 2018 to Jun 2021**")
   st.write('*Responsibilities:*')
   st.caption("⚒️  Worked across products, consulting and delivery divisions facilitating cross pollination of ideas and contributed to multiple analytics projects.")
   st.caption("⚒️  Spearheaded multiple marketing analytics engagement across multiple domains helping the clients to get insights out of data and enabling the clients to save more than100K dollars in stream-lining their marketing operations.")
   st.caption("⚒️  As a product manager, performed market scoping and identified new markets for the product through market research and conducted market assessment to identify potential opportunities and market fit for the product. Collaborated with Developers, Data Engineers, UX designers, and the testing team to provide quality deliverables .Also, coordinated among stakeholders to create a product roadmap and product requirement documents.")
   st.caption("⚒️  Conducted sessions on Python, MS-Excel and Case Studies for the new joinees.")
   st.divider()
   st.subheader(':blue[Experience-Pre MBA]')
   st.write('**Infosys Technologies - Technology Analyst - April 2015- June 2016**')
   st.write('*Responsibilities:*')
   st.caption("⚒️  Worked on Mainframe projects associated with Wal-Mart covering the entire spectrum of Software Development Life Cycle.")
   st.caption("⚒️  Spearheaded the implementation and development activities from Sao Paulo, Brazil.")
   st.divider()
   st.write('**Cognizant Technology Solutions - Programmer Analyst - Dec 2011- March 2015**')
   st.write('*Responsibilities:*')
   st.caption("⚒️  Executed multiple mainframe projects for various Healthcare Accounts like UHG, predominantly on the claims processing & report generation.")
   st.caption("⚒️  Played the role of a techno-functional consultant for Cognizant Business Consulting (CBC) Healthcare division, imparting technical understanding to the BA and Consultant about a Claims processing system.")
   st.divider()
#with st.container():
   st.subheader(':blue[Skills]')
    # col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    # with col1:
    #     st_lottie(python_lottie, height=70,width=70, key="python", speed=2.5)
    # with col2:
    #     st_lottie(java_lottie, height=70,width=70, key="java", speed=4)
    # with col3:
    #     st_lottie(my_sql_lottie,height=70,width=70, key="mysql", speed=2.5)
    # with col4:
    #     st_lottie(git_lottie,height=70,width=70, key="git", speed=2.5)
    # with col1:
    #     st_lottie(github_lottie,height=50,width=50, key="github", speed=2.5)
    # with col2:
    #     st_lottie(docker_lottie,height=70,width=70, key="docker", speed=2.5)
    # with col3:
    #     st_lottie(figma_lottie,height=50,width=50, key="figma", speed=2.5)
    # with col4:
    #     st_lottie(js_lottie,height=50,width=50, key="js", speed=1)
   text = 'Python,Python,Python,PowerBI,SQL,SQL,MachineLearning,MachineLearning,DataAnalytics,DataAnalytics,'
   text1= 'Azure,Azure,PowerBI,DataEngineering,GenerativeAI,GenerativeAI,DataStrategy,DataVisualization,DataProducts'
   text2= 'RequirementGathering,RequirementGathering,Roadmapping,Workshop,Jira,Confluence,AzureDevops,Advisory,Agile,Agile,Waterfall,TeamManagemnet,CrossCollaboration,StakeholderManagement'
   text3='Insurance,Insurance,FMCG,FMCG,Pharma,Pharma,Retail,EIS Suite'
   text=text + text1


# Create and generate a word cloud image:
   wordcloud = WordCloud(background_color='white',
                            collocations=False,
                            width=300,
                            height=250,
                            contour_width=1,
                            contour_color='black').generate(text)
   wordcloud1 = WordCloud(background_color='white',
                            collocations=False,
                            width=300,
                            height=250,
                            contour_width=1,
                            contour_color='black').generate(text2)
   wordcloud2 = WordCloud(background_color='white',
                            collocations=False,
                            width=300,
                            height=250,
                            contour_width=1,
                            contour_color='black').generate(text3)
   c11,c12,c13=st.columns(3)
# Display the generated image:
    #st.write("Programming Language")
    # plt.figure(figsize = (8, 8), facecolor = None)
    # plt.imshow(wordcloud)
    # plt.axis("off")
    # plt.tight_layout(pad = 0)
    #st.write(wordcloud)
   with c11:
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()
   with c12:
        plt.imshow(wordcloud1, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()
   with c13:
        plt.imshow(wordcloud2, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()
if selected=='Projects':
   st.markdown('**Project Name:** WEG')
   st.markdown('Client: Global Insurance Provider')
   st.markdown('Domain: Data Engineering/Business Intelligence')
   st.markdown('Objective: Process data from New Channel that organizantion has introduced to sell its policies. Also to capture key business metrics (KPI) for the new channel.')
   st.markdown("""Roles & Responsibility:
   -   Worked as the Lead Consultant helping the delivery team to create necessary solution by performing the initial analysis of the data and suggesting the approach to achieve necessary business goal.
   -   Coordinated with Business Owner to  prioritize user stories and  created wireframes for the new reports.
   -   SME for EIS System and Reference Data Management.
   -   Showcased the demo of the dashboard/report to End-Business users.
   -   Provided strategic roadmap & tactical assistance to Senior Directors and AVP, helping them to shape key initiatives for organizations growth.
   """)

   st.markdown('**Project Name:** Connectik')
   st.markdown('Client: Global Lifesciences Company')
   st.markdown('Domain: Business Intelligence/Analytics')
   st.markdown('Objective: Create dashboards and analytical solutions to provide visibity into sales & marketing oporations support sales and marketing team of different product lines.')
   st.markdown("""Roles & Responsibility:
   -   Worked as the Lead Consultant anchoring the requirement gathering workshop with stakeholders.
   -   Created Artefacts such as BRD collborating with business users, FRD , user manual
   -   Conducted UAT sessions coordinating with the testing team, created same data and business scenarios to support testing.
   -   Played a key role in transitioning the team from waterfall model of delivery to agile. Took additional responsibility as Scrum Master and Managed Azure Devops board.  
   -   Worked with Data Scientist to develop Churn Prediction Model and Customer Segmentation model.
   """)
   
   # st.write('Roles & Responsibility')
   # st.markdown("        ⚒️  Worked as the Lead Consultant helping the delivery team to create necessary solution by performing the initial analysis of the data and suggesting the approach to achieve necessary business goal.")
   # st.caption("        ⚒️  As a part of this engagement, multiple reports such as commission, fraudulent reports are generated out of the data platform and provided to end business user to make business decisions.  In addition to the reports, key KPIs are captured in the form of Power BI Dashboards to support business users day to day activities.")
   # st.caption("        ⚒️  The role involves in providing strategic roadmap & tactical assistance to senior directors and AVP, helping them to shape key initiatives for organizations growth.")
   # st.caption("        ⚒️  SME for EIS system (Insurance System used for creating customer, policy, claim) and Reference Data Management.")

   # st.write('*Project 2*')
   # st.caption("⚒️  Providing strategic roadmap & tactical assistance to senior directors and AVP, helping them to shape key initiatives for fuelling organizational growth.")
   # st.caption("⚒️  Day to day activities involves requirement gathering, converting the technical requirement into business requirement. Addressing concerns/questions on the data platform from stakeholders. Showing the demo of the newly introduced features.")
   # st.caption("⚒️  Aiding internal sales teamon responding to RFI/RFP by understanding the business & industry landscape and providing relevant frameworks,case studies to build a more concrete proposal.")
   # st.caption("⚒️  Supporting Recruitment drives to hire right set of candidates for the organization.")

if selected=='Data Products':
   st.markdown('Product Name: :blue[Smart Insights]')
   st.markdown('About the Product: SmartInsights is a social media listening tool helping the marketing function of an organization to identify trends, brand strength, influencers and craft branding message')
   st.markdown('Domain: Global Lifesciences/CPG Company')
   #st.markdown('Domain: Business Intelligence/Analytics')
   #st.markdown('Objective: Create dashboards and analytical solutions to provide visibity into sales & marketing oporations support sales and marketing team of different product lines.')
   st.markdown("""Roles & Responsibility:
   -   Managed the product from ideation to launch and beyond.
   -   Performed market scoping and identified new markets for the product through market research.
   -   Conducted market assessment to identify potential opportunities and market fit for the product.
   -   Coordinated with CPO/CTO to create a product roadmap and product requirement documents as part of the product management team.
   -   Demonstrated the capability of the product to prospective clients and conducted workshops/functional training sessions to the end-users on the product usage.  
   -   Worked alongside data science team on trend analysis and trend scoring module.
   -   Managed engagements worth 200K USD for multiple CPG companies operating across multiple categories and multiple geographies.
   """)
   st.divider()
   st.markdown('Product Name: :blue[Contract Analyser]')
   st.markdown('About the Product:Contract Analyser is a NLP based analytics solution helping the procurement/finance function of an organization to extract key insights from the contract and providing suitable intervention to the stakeholders to mitigate any financial loss.')
   st.markdown('Domain: Domain Agnostic')
   #st.markdown()
   #st.markdown('Client: Global Lifesciences Company')
   #st.markdown('Domain: Business Intelligence/Analytics')
   #st.markdown('Objective: Create dashboards and analytical solutions to provide visibity into sales & marketing oporations support sales and marketing team of different product lines.')
   st.markdown("""Roles & Responsibility:
   -   Responsible for sales and marketing activities for the Product. Some of the activities includes preparing sales deck, publishing blogs on contract analytics. Benchmarking the product against the competitor and executing an outreach email-campaign using Pardot. 
   -   Created marketing artefacts (Blog, Infographic, Reach out messages) for the product.
   -   Collaborated with Data Scientists, Data Engineers, UX Designers and the testing team to rollout features/customization to the customers. Extensively worked on Named Entity Recogniztion module to indentify key information from contracts. 
   -   Defined and tracked KPIs to measure the success of AI products.
   -   Used data-driven insights to prioritize features and optimize user experience.
   """)
   st.divider()
   st.markdown('Product Name: :blue[Internal Product]')
   st.markdown('Domain: Lifesciences')
   st.markdown('About the Product: This product is an analytics solution helping the sales/marketing function of the organization to provide customer insights,identify customer churms and perform customer segmentation.')
   #st.markdown()
   #st.markdown('Client: Global Lifesciences Company')
   #st.markdown('Domain: Business Intelligence/Analytics')
   #st.markdown('Objective: Create dashboards and analytical solutions to provide visibity into sales & marketing oporations support sales and marketing team of different product lines.')
   st.markdown("""Roles & Responsibility:
   -   Worked as the Lead Product Consultant anchoring the requirement gathering workshop with stakeholders and managing multiple streams.
   -   Created Artefacts such as BRD collborating with business users, FRD , user manual
   -   Conducted UAT sessions coordinating with the testing team, created sample data and business scenarios to support testing.
   -   Played a key role in transitioning the team from waterfall model of delivery to agile. Took additional responsibility as Scrum Master and Managed Azure Devops board.  
   -   Worked with Data Scientist to develop Churn Prediction Model and Customer Segmentation model.
   -   Mentored and guided junior team members.
   """)
   # st.subheader(':blue[FMCG]')
   # st.write("⚒️ Social Media Analytics")
   # st.write("⚒️ E-commerce & Competitor Analysis")
   # st.write("⚒️ Marketing Mix Modelling")
   # st.divider()
   # st.subheader(':blue[Retail/E-Commerce]')
   # st.write("⚒️ Market Basket Analysis")
   # st.write("⚒️ RFM Analysis")
   # st.write("⚒️ Customer Data Platform")
   # st.divider()
   # st.subheader(':blue[Insurance]')
   # st.write("⚒️ Fraud Detection")
   # st.write("⚒️ Data Platform")
   # st.write("⚒️ Omni-channel Marketing & Customer Journey")
   # st.divider()
   # st.subheader(':blue[Life Sciences]')
   # st.write("⚒️ Sales Analytics ")
   # st.write("⚒️ Churn Prediction")
   # st.write("⚒️ Customer Segmentation")
if selected=='Gen AI Products':
   st.markdown('Product Name: :blue[Synthetic Data Generator]')
   st.markdown('About the Product: Synthetic Data Generator is an internal Gen AI tool helping the testing and data science team to address ethical concerns and lack/unavailability of data.')
   st.markdown('Domain: Global Lifesciences')
   #st.markdown('Domain: Business Intelligence/Analytics')
   #st.markdown('Objective: Create dashboards and analytical solutions to provide visibity into sales & marketing oporations support sales and marketing team of different product lines.')
   st.markdown("""Roles & Responsibility:
   -   Worked with UX team to design the tool. Developed wireframes/workflow using streamlit.
   -   Provided training and insights about the tool with larger audience
   -   Worked closely with Data Leads to define AI Governance, best practises,responsible AI charter for the organization.
   """)
   st.divider()
   st.markdown('Product Name: :blue[I-Ask]')
   st.write("This Gen AI tool is a knowledge management tool for insurance domain helping the user in understanding various terminology associated with the insurance industry.")
   st.markdown("""Roles & Responsibility:
   -   Identification of data sources to be fed into the Large Language Model.
   -   Provided training and insights about the tool with larger audience.
   -   Model evaluation/testing to test for performance and hallucination.
   -   Act as the liason between technical teams and non-technical stakeholders, ensuring clear communication and removing impediments.
   """)
   st.divider()
   st.subheader(':blue[Learning & Training]')
   st.write("Conducted training sessions for the associate on potential & usage of Gen AI")
   st.write("Evaluated Hackthons on Gen AI and provided feedback.")
if selected=='Education':
   st.subheader(':blue[Under-Graduation]')
   st.write("**Course     - Computer Science & Engineering.**")
   st.write("**College    - St.Peters Enginnering College.**")
   st.write("**University - Anna University,Chennai.**")
   st.write("**Percentage - 74.3%**")
   #st.write("Project 1- Leading Insurance Company")
   st.write('*Achievements*')
   st.caption("Won multiple quiz compettitions held at various colleges in Chennai.")
   st.divider()
   st.subheader(':blue[Post-Graduation]')
   st.write("**Course     - Post Graduate Diploma in Management (PGDM/MBA).**")
   st.write("**Institute  - Indian Institute of Management, Kashipur**")
   st.write("**CGPA       - 74.3%**")
   st.write('*Achievements*')
   st.caption("Received top grades in ERP, Marketing Analytics, Business Intelligence, Social Media Analytics, Data Science & Business Analytics.")
   st.caption("Runner up on a case study competition conducted by IIM Udaipur & published an article on startup ecosystem with IIT Bombay.")
   st.divider()
   #st.write("Project 1- Leading Insurance Company")
   st.subheader(':blue[Certifications]') 
      
   c1,c2,c3=st.columns(3)
   with c1:
        st.write("  AI Fundamentals  ")
        st.image('AI900.JPG')
   with c2:
        st.write("  Azure Fundamentals  ")
        st.image('AZ900.JPG')
   with c3:
        st.write("  PowerBI  ")
        st.image('PL-300.JPG')
# -----------------  Downloads  ----------------- #
if selected=='Resume':
   file1=r"Dingoo Karthick_G.pdf"
   #st.write("View Resume")
   displayPDF(file1)
#    with open(file1, "rb") as file:
#             btn = st.download_button(
#             label=":blue[Download Resume]",
#             data=file,
#             file_name="dingoo.pdf",
#             mime="pdf"
#           )
# # -----------------  contact  ----------------- #
if selected=='Contact Me':
        st.subheader("📨 Contact Me")
        contact_form = f"""
        <form action="https://formsubmit.co/karthickg12@gmail.com" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
        local_css("style.css")

