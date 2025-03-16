##Environment Configuration
Create an .env file in the root directory of your project with the following structure:
```
juhe_financial_news_token = "YOUR JUHE FINANCIAL TOKEN (OPTIONAL)"
newsapi = "YOUR FINANCIAL NEWS TOKEN (OPTIONAL)"

Siliconflow_api_key = "YOUR SILICONFLOW TOKEN"

NEO4J_URI = "YOUR NEO4J URI"
NEO4J_USERNAME = "YOUR NEO4J USERNAME (USUALLY neo4j)"
NEO4J_PASSWORD = "YOUR NEO4J PASSWORD"
```
Notes:
juhe_financial_news_token and newsapi are optional and not strictly required.
Replace each placeholder with your actual credentials.

##Installation
Since LightRAG currently does not have an official released version, you'll need to install it manually. First, download the LightRAG repository from GitHub. Once downloaded, navigate to the folder containing the repository and install it using pip:
```
cd LightRAG  # replace with your actual downloaded path
pip install -e .
```
For additional details and complete installation instructions, please refer to the official LightRAG documentation on their GitHub repository:

https://github.com/HKUDS/LightRAG
