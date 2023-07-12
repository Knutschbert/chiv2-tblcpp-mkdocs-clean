---
title: UTBLQuestsBlueprintLibrary
type: class
aliases: UTBLQuestsBlueprintLibrary
share: false

---

# UTBLQuestsBlueprintLibrary





Inherits from UBlueprintFunctionLibrary

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[CampaignLevelHasPremiumReward]]**(const [FCampaignLevel](/docs/SDK/Source/Classes/structFCampaignLevel.md) & Level) |
| bool | **[[GetCampaignPurchasingEnabled]]**(UObject * WorldContextObject) |
| bool | **[[GetCampaignsEnabled]]**(UObject * WorldContextObject) |
| bool | **[[GetQuestsEnabled]]**(UObject * WorldContextObject) |
| ETBLRarity | **[[GetRewardItemRarity]]**(const FPrimaryAssetId & PrimaryAssetId) |
| UTexture2D * | **[[GetTextureFromSlateBrush]]**(const FSlateBrush & Brush) |
| TArray< [FQuestReward](/docs/SDK/Source/Classes/structFQuestReward.md) > | **[[GetUnlockedRewardsForCampaignLevel]]**(TScriptInterface< [ICampaign](/docs/SDK/Source/Classes/classICampaign.md) > Campaign, int32 Level, bool CheckPremiumPurchase) |
| bool | **[[IsCampaignOwned]]**(TScriptInterface< [ICampaignPurchasable](/docs/SDK/Source/Classes/classICampaignPurchasable.md) > Campaign, UObject * WorldContextObject) |
| bool | **[[IsPrimaryAssetIdCampaign]]**(const FPrimaryAssetId & PrimaryAssetId) |
| bool | **[[IsStoreOfferIdCampaign]]**(const FString & OfferId) |
| void | **[[OnCampaignListReady]]**(APlayerController * PC, FOnCampaignListReady NewOnCampaignListReady) |
| | **[[UTBLQuestsBlueprintLibrary]]**() |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200