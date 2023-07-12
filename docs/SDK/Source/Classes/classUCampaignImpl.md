---
title: UCampaignImpl
type: class
aliases: UCampaignImpl
share: false

---

# UCampaignImpl





Inherits from [UReplicatedSubobject](/docs/SDK/Source/Classes/classUReplicatedSubobject.md), [ICampaign](/docs/SDK/Source/Classes/classICampaign.md), [ICampaignPurchasable](/docs/SDK/Source/Classes/classICampaignPurchasable.md), [IQuest](/docs/SDK/Source/Classes/classIQuest.md), [IQuestDisplayable](/docs/SDK/Source/Classes/classIQuestDisplayable.md), UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void void void | **[[BindOnCompleted]]**(const FOnQuestCompleteChanged & Delegate) override |
| virtual void void | **[[BindOnLevelChanged]]**(const FOnCampaignLevelChanged & Delegate) override |
| virtual void void | **[[BindOnProgressChanged]]**(const FOnQuestProgressChanged & Delegate) override |
| virtual void | **[[BindOnPurchasedChanged]]**(const FOnCampaignPurchasedChanged & Delegate) override |
| virtual void | **[[BindOnTimedQuestStatusChanged]]**(const FOnTimedQuestStatusChanged & Delegate) override |
| virtual void | **[[BindOnXpChanged]]**(const FOnCampaignXpChanged & Delegate) override |
| FText return | **[[FText::GetEmpty]]**() |
| FText return | **[[FText::GetEmpty]]**() |
| FText return | **[[FText::GetEmpty]]**() |
| FText return | **[[FText::GetEmpty]]**() |
| FText return | **[[FText::GetEmpty]]**() |
| FText return | **[[FText::GetEmpty]]**() |
| virtual TScriptInterface< [IQuest](/docs/SDK/Source/Classes/classIQuest.md) > | **[[GetActiveQuest]]**() const override |
| virtual TArray< [FCampaignLevel](/docs/SDK/Source/Classes/structFCampaignLevel.md) > | **[[GetAllLevelDetails]]**() const override |
| virtual TSoftObjectPtr< UTexture2D > | **[[GetBannerImage]]**() const override |
| virtual int32 | **[[GetCurrentLevelMaxXp]]**() const override |
| virtual int32 | **[[GetCurrentLevelXp]]**() const override |
| virtual FText | **[[GetDescription]]**() const override |
| virtual EQuestDifficulty | **[[GetDifficulty]]**() const override |
| virtual FString | **[[GetFriendlyName]]**() const override |
| virtual int32 | **[[GetGatedMaxLevel]]**() const override |
| virtual FText | **[[GetGoalText]]**() const override |
| virtual TSoftObjectPtr< UTexture2D > | **[[GetIcon]]**() const override |
| virtual int32 | **[[GetLevel]]**() const override |
| virtual [FCampaignLevel](/docs/SDK/Source/Classes/structFCampaignLevel.md) | **[[GetLevelDetails]]**() const override |
| virtual int32 | **[[GetLevelFromItemId]]**(const FPrimaryAssetId & ItemId) override |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| virtual FText | **[[GetMaxScoreText]]**() const override |
| virtual int32 | **[[GetNumLevels]]**() const override |
| virtual float | **[[GetProgress]]**() const override |
| virtual TArray< [FQuestReward](/docs/SDK/Source/Classes/structFQuestReward.md) > | **[[GetRewards]]**() const override |
| virtual FText | **[[GetScoreText]]**() const override |
| virtual FText | **[[GetShortDescription]]**() const override |
| virtual FString | **[[GetStoreOfferId]]**() const override |
| virtual [FStoreOfferItem](/docs/SDK/Source/Classes/structFStoreOfferItem.md) | **[[GetStoreOfferItem]]**() const override |
| virtual FTimespan | **[[GetTimeRemaining]]**() const override |
| virtual FText | **[[GetTitle]]**() const override |
| virtual void void void TSoftObjectPtr< UTexture2D > | **[[GetTitleImage]]**() const override |
| virtual int32 | **[[GetTotalMaxXp]]**() const override |
| virtual int32 | **[[GetTotalXp]]**() const override |
| virtual void void bool | **[[HasPremiumRewards]]**() const override |
| virtual bool | **[[IsClientAuthoritative]]**() const override |
| virtual bool | **[[IsComplete]]**() const override |
| virtual bool | **[[IsExpired]]**() const override |
| virtual void void void void bool | **[[IsPurchased]]**() const override |
| virtual bool | **[[IsTimeAvailable]]**() const override |
| virtual bool | **[[IsTimed]]**() const override |
| virtual void void void void bool | **[[IsUpcoming]]**() const override |
| void | **[[OnRep_AttachedPlayerState]]**(const [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * PreviousAttachedPlayerState) |
| void | **[[OnRep_BackendId]]**(const FString & PreviousBackendId) |
| virtual void void void void | **[[SetPurchased]]**() override |
| TArray< [FCampaignLevel](/docs/SDK/Source/Classes/structFCampaignLevel.md) > return | **[[TArray]]**() |
| TArray< [FQuestReward](/docs/SDK/Source/Classes/structFQuestReward.md) > return | **[[TArray]]**() |
| FString return | **[[TEXT]]**("" ) |
| FString return | **[[TEXT]]**("" ) |
| | **[[UCampaignImpl]]**() |
| virtual void void void void | **[[UnbindOnCompleted]]**(const FOnQuestCompleteChanged & Delegate) override |
| virtual void void | **[[UnbindOnLevelChanged]]**(const FOnCampaignLevelChanged & Delegate) override |
| virtual void void void | **[[UnbindOnProgressChanged]]**(const FOnQuestProgressChanged & Delegate) override |
| virtual void void void | **[[UnbindOnPurchasedChanged]]**(const FOnCampaignPurchasedChanged & Delegate) override |
| virtual void void | **[[UnbindOnTimedQuestStatusChanged]]**(const FOnTimedQuestStatusChanged & Delegate) override |
| virtual void | **[[UnbindOnXpChanged]]**(const FOnCampaignXpChanged & Delegate) override |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FCampaignLevel](/docs/SDK/Source/Classes/structFCampaignLevel.md) return | **[[FCampaignLevel]]**  |
| [FStoreOfferItem](/docs/SDK/Source/Classes/structFStoreOfferItem.md) return | **[[FStoreOfferItem]]**  |
| FTimespan return | **[[FTimespan]]**  |
| TScriptInterface< [IQuest](/docs/SDK/Source/Classes/classIQuest.md) > return | **[[NULL]]**  |
| void void void TSoftObjectPtr< UTexture2D > return | **[[NULL]]**  |
| TSoftObjectPtr< UTexture2D > return | **[[NULL]]**  |
| [FCampaignImplSpecData](/docs/SDK/Source/Classes/structFCampaignImplSpecData.md) | **[[SpecData]]**  |
| FTimerHandle | **[[TimedCampaignStatusChangeTimer]]**  |
| bool | **[[bUploadToBackend]]**  |
| void void bool return | **[[false]]**  |
| void void void void bool return | **[[false]]**  |
| void void bool return | **[[false]]**  |
| int32 | **[[return]]**  |
| float | **[[return]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200