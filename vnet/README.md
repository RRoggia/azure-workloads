## Create vnet

az network vnet create -n roggia-vnet -g $az_rg --address-prefix 15.0.0.0/16 


## Create subnet

az network vnet subnet create -n sub1 -g $az_rg --vnet-name roggia-vnet --address-prefix "15.0.0.0/24"
az network vnet subnet create -n sub2 -g $az_rg --vnet-name roggia-vnet --address-prefix "15.0.1.0/24"

## Create P ip
az network public-ip create -g $az_rg -n roggia-ag-pip


## Create App Gateway

az network application-gateway create -n roggia-ag -g $az_rg --capacity 2 --subnet sub1 --vnet-name roggia-vnet
