---
title: ICampaign
type: class
aliases: ICampaign
share: false

---

# ICampaign





Inherits from IInterface

Inherited by [UCampaignImpl](/docs/SDK/Source/Classes/classUCampaignImpl.md), [UCampaignStub](/docs/SDK/Source/Classes/classUCampaignStub.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void virtual void | **[[BindOnLevelChanged]]**(const FOnCampaignLevelChanged & Delegate) |
| virtual void | **[[BindOnXpChanged]]**(const FOnCampaignXpChanged & Delegate) |
| virtual TScriptInterface< [IQuest](/docs/SDK/Source/Classes/classIQuest.md) > | **[[GetActiveQuest]]**() const |
| virtual TArray< [FCampaignLevel](/docs/SDK/Source/Classes/structFCampaignLevel.md) > | **[[GetAllLevelDetails]]**() const |
| virtual int32 | **[[GetCurrentLevelMaxXp]]**() const |
| virtual int32 | **[[GetCurrentLevelXp]]**() const |
| virtual FString | **[[GetFriendlyName]]**() const |
| virtual int32 | **[[GetGatedMaxLevel]]**() const |
| virtual int32 | **[[GetLevel]]**() const |
| virtual [FCampaignLevel](/docs/SDK/Source/Classes/structFCampaignLevel.md) | **[[GetLevelDetails]]**() const |
| virtual int32 | **[[GetLevelFromItemId]]**(const FPrimaryAssetId & ItemId) |
| virtual int32 | **[[GetNumLevels]]**() const |
| virtual int32 | **[[GetTotalMaxXp]]**() const |
| virtual int32 | **[[GetTotalXp]]**() const |
| virtual void virtual void virtual bool | **[[HasPremiumRewards]]**() const |
| TArray< [FCampaignLevel](/docs/SDK/Source/Classes/structFCampaignLevel.md) > return | **[[TArray]]**() |
| FString return | **[[TEXT]]**("" ) |
| virtual void virtual void | **[[UnbindOnLevelChanged]]**(const FOnCampaignLevelChanged & Delegate) |
| virtual void | **[[UnbindOnXpChanged]]**(const FOnCampaignXpChanged & Delegate) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FCampaignLevel](/docs/SDK/Source/Classes/structFCampaignLevel.md) return | **[[FCampaignLevel]]**  |
| TScriptInterface< [IQuest](/docs/SDK/Source/Classes/classIQuest.md) > return | **[[NULL]]**  |
| void virtual void virtual bool return | **[[false]]**  |
| int32 | **[[return]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200