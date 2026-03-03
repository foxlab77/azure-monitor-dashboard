# Variables
$location = "uksouth"
$rg = "rg-dashboard-day3"
$plan = "plan-dashboard-day3"
$app = "dashboardday3ukjp$(Get-Random -Maximum 9999)"

Write-Host "Creating Resource Group..."
az group create --name $rg --location $location

Write-Host "Creating App Service Plan..."
az appservice plan create `
    --name $plan `
    --resource-group $rg `
    --sku B1 `
    --is-linux

Write-Host "Creating Web App..."
az webapp create `
    --resource-group $rg `
    --plan $plan `
    --name $app `
    --runtime "PYTHON:3.11"

Write-Host "Deploying app..."
az webapp up `
    --name $app `
    --resource-group $rg `
    --runtime "PYTHON:3.11"

Write-Host "Setting startup command..."
az webapp config set `
    --resource-group $rg `
    --name $app `
    --startup-file "gunicorn --bind=0.0.0.0:8000 wsgi:app"

Write-Host "Setting environment variable..."
az webapp config appsettings set `
    --resource-group $rg `
    --name $app `
    --settings ENVIRONMENT=production

Write-Host "Deployment complete!"
Write-Host "App name: $app"