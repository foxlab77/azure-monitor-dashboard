# Could not login to foxlab77@gmail.com with az cli in VSCode

# Create the resource group
az group create --name rg-dashboard-day3 --location polandcentral

# Create the app service plan
az appservice plan create --name plan-dashboard-day3 --resource-group rg-dashboard-day3 --sku F1 --is-linux --location polandcentral

# Create the web app
az webapp create --resource-group rg-dashboard-day3 --plan plan-dashboard-day3 --name dashboardday3ukjp0103 --runtime "PYTHON:3.11"

# Deploy the app
az webapp up --name dashboardday3ukjp0301 --resource-group rg-dashboard-day3 --runtime "PYTHON:3.11"

# Set startup command
az webapp config set --resource-group rg-dashboard-day3 --name dashboardday3ukjp0103 --startup-file "gunicorn --bind=0.0.0.0:8000 wsgi:app"

# Set environment variable
az webapp config appsettings set --resource-group rg-dashboard-day3 --name dashboardday3ukjp0103 --settings ENVIRONMENT=production

#Test the site
az webapp show --resource-group rg-dashboard-day3 --name dashboardday3ukjp0103 --query defaultHostName -o tsv