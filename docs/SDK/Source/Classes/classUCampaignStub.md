---
title: UCampaignStub
type: class
aliases: UCampaignStub
share: false

---

# UCampaignStub





Inherits from UObject, [ICampaign](/docs/SDK/Source/Classes/classICampaign.md), [IQuest](/docs/SDK/Source/Classes/classIQuest.md), [IQuestDisplayable](/docs/SDK/Source/Classes/classIQuestDisplayable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void void void | **[[BindOnCompleted]]**(const FOnQuestCompleteChanged & Delegate) override |
| virtual void void | **[[BindOnLevelChanged]]**(const FOnCampaignLevelChanged & Delegate) override |
| virtual void void | **[[BindOnProgressChanged]]**(const FOnQuestProgressChanged & Delegate) override |
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
| virtual FText | **[[GetMaxScoreText]]**() const override |
| virtual int32 | **[[GetNumLevels]]**() const override |
| virtual float | **[[GetProgress]]**() const override |
| virtual TArray< [FQuestReward](/docs/SDK/Source/Classes/structFQuestReward.md) > | **[[GetRewards]]**() const override |
| virtual FText | **[[GetScoreText]]**() const override |
| virtual FText | **[[GetShortDescription]]**() const override |
| virtual FTimespan | **[[GetTimeRemaining]]**() const override |
| virtual FText | **[[GetTitle]]**() const override |
| virtual void void void TSoftObjectPtr< UTexture2D > | **[[GetTitleImage]]**() const override |
| virtual int32 | **[[GetTotalMaxXp]]**() const override |
| virtual int32 | **[[GetTotalXp]]**() const override |
| virtual void void bool | **[[HasPremiumRewards]]**() const override |
| virtual bool | **[[IsClientAuthoritative]]**() const override |
| virtual bool | **[[IsComplete]]**() const override |
| virtual bool | **[[IsExpired]]**() const override |
| virtual bool | **[[IsTimeAvailable]]**() const override |
| virtual bool | **[[IsTimed]]**() const override |
| virtual void void void void void bool | **[[IsUpcoming]]**() const override |
| TArray< [FCampaignLevel](/docs/SDK/Source/Classes/structFCampaignLevel.md) > return | **[[TArray]]**() |
| TArray< [FQuestReward](/docs/SDK/Source/Classes/structFQuestReward.md) > return | **[[TArray]]**() |
| FString return | **[[TEXT]]**("" ) |
| | **[[UCampaignStub]]**() |
| virtual void void void void void | **[[UnbindOnCompleted]]**(const FOnQuestCompleteChanged & Delegate) override |
| virtual void void | **[[UnbindOnLevelChanged]]**(const FOnCampaignLevelChanged & Delegate) override |
| virtual void void void void | **[[UnbindOnProgressChanged]]**(const FOnQuestProgressChanged & Delegate) override |
| virtual void void void | **[[UnbindOnTimedQuestStatusChanged]]**(const FOnTimedQuestStatusChanged & Delegate) override |
| virtual void | **[[UnbindOnXpChanged]]**(const FOnCampaignXpChanged & Delegate) override |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FCampaignLevel](/docs/SDK/Source/Classes/structFCampaignLevel.md) return | **[[FCampaignLevel]]**  |
| FTimespan return | **[[FTimespan]]**  |
| TScriptInterface< [IQuest](/docs/SDK/Source/Classes/classIQuest.md) > return | **[[NULL]]**  |
| void void void TSoftObjectPtr< UTexture2D > return | **[[NULL]]**  |
| TSoftObjectPtr< UTexture2D > return | **[[NULL]]**  |
| void void bool return | **[[false]]**  |
| void void void void void bool return | **[[false]]**  |
| void void bool return | **[[false]]**  |
| int32 | **[[return]]**  |
| float | **[[return]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200