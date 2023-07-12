---
title: UCampaignList
type: class
aliases: UCampaignList
share: false

---

# UCampaignList





Inherits from UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AbandonAllCampaigns]]**() |
| void | **[[AbandonCampaign]]**(UObject * CampaignObject) |
| void | **[[FixPurchasedCampaignStateIfNeeded]]**(TScriptInterface< [ICampaignPurchasable](/docs/SDK/Source/Classes/classICampaignPurchasable.md) > PurchasableCampaign) |
| TArray< TScriptInterface< [ICampaign](/docs/SDK/Source/Classes/classICampaign.md) > > | **[[GetActiveCampaigns]]**() |
| TArray< TScriptInterface< [ICampaign](/docs/SDK/Source/Classes/classICampaign.md) > > | **[[GetAllCampaigns]]**() const |
| TScriptInterface< [ICampaign](/docs/SDK/Source/Classes/classICampaign.md) > | **[[GetCampaignForPremiumGood]]**(const FPrimaryAssetId & PremiumGoodId) |
| TScriptInterface< [ICampaign](/docs/SDK/Source/Classes/classICampaign.md) > | **[[GetCampaignForStoreOffer]]**(const FString & StoreOfferId) |
| TScriptInterface< [ICampaign](/docs/SDK/Source/Classes/classICampaign.md) > | **[[GetCampaignIdFromItemAssetId]]**(const FPrimaryAssetId & ItemId) |
| TScriptInterface< [ICampaign](/docs/SDK/Source/Classes/classICampaign.md) > | **[[GetCampaignWithId]]**(const FString & ID) |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| TArray< TScriptInterface< [ICampaign](/docs/SDK/Source/Classes/classICampaign.md) > > | **[[GetOwnedCampaigns]]**() |
| bool | **[[IsCampaignActive]]**(TScriptInterface< [ICampaign](/docs/SDK/Source/Classes/classICampaign.md) > Campaign) const |
| void | **[[OnReady]]**(FOnCampaignsChangedDelegate NewOnReady) |
| void | **[[OnTimedCampaignStatusChanged]]**([UCampaignImpl](/docs/SDK/Source/Classes/classUCampaignImpl.md) * Campaign) |
| TScriptInterface< [ICampaign](/docs/SDK/Source/Classes/classICampaign.md) > | **[[SlotCampaign]]**(TScriptInterface< [ICampaign](/docs/SDK/Source/Classes/classICampaign.md) > Campaign) |
| | **[[UCampaignList]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FOnCampaignsChanged | **[[OnActiveCampaignChanged]]**  |
| FOnCampaignsChanged | **[[OnCampaignsChanged]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200