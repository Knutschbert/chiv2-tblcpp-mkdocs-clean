---
title: UAchievementQuest
type: class
aliases: UAchievementQuest
share: false

---

# UAchievementQuest





Inherits from UObject, [IQuest](/docs/SDK/Source/Classes/classIQuest.md), [IQuestDisplayable](/docs/SDK/Source/Classes/classIQuestDisplayable.md), [IQuestReplicatable](/docs/SDK/Source/Classes/classIQuestReplicatable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void void void | **[[BindOnCompleted]]**(const FOnQuestCompleteChanged & Delegate) override |
| virtual void void | **[[BindOnProgressChanged]]**(const FOnQuestProgressChanged & Delegate) override |
| virtual void | **[[BindOnTimedQuestStatusChanged]]**(const FOnTimedQuestStatusChanged & Delegate) override |
| FText return | **[[FText::GetEmpty]]**() |
| FText return | **[[FText::GetEmpty]]**() |
| FText return | **[[FText::GetEmpty]]**() |
| FText return | **[[FText::GetEmpty]]**() |
| FText return | **[[FText::GetEmpty]]**() |
| FText return | **[[FText::GetEmpty]]**() |
| virtual TSoftObjectPtr< UTexture2D > | **[[GetBannerImage]]**() const override |
| virtual FText | **[[GetDescription]]**() const override |
| virtual EQuestDifficulty | **[[GetDifficulty]]**() const override |
| virtual FText | **[[GetGoalText]]**() const override |
| virtual TSoftObjectPtr< UTexture2D > | **[[GetIcon]]**() const override |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| virtual FText | **[[GetMaxScoreText]]**() const override |
| virtual float | **[[GetProgress]]**() const override |
| virtual TArray< [FQuestReward](/docs/SDK/Source/Classes/structFQuestReward.md) > | **[[GetRewards]]**() const override |
| virtual FText | **[[GetScoreText]]**() const override |
| virtual FText | **[[GetShortDescription]]**() const override |
| virtual FTimespan | **[[GetTimeRemaining]]**() const override |
| virtual FText | **[[GetTitle]]**() const override |
| virtual void void void TSoftObjectPtr< UTexture2D > | **[[GetTitleImage]]**() const override |
| virtual bool | **[[IsClientAuthoritative]]**() const override |
| virtual bool | **[[IsComplete]]**() const override |
| virtual bool | **[[IsExpired]]**() const override |
| virtual bool | **[[IsTimeAvailable]]**() const override |
| virtual bool | **[[IsTimed]]**() const override |
| virtual void void void bool | **[[IsUpcoming]]**() const override |
| TArray< [FQuestReward](/docs/SDK/Source/Classes/structFQuestReward.md) > return | **[[TArray]]**() |
| | **[[UAchievementQuest]]**() |
| virtual void void void | **[[UnbindOnCompleted]]**(const FOnQuestCompleteChanged & Delegate) override |
| virtual void void | **[[UnbindOnProgressChanged]]**(const FOnQuestProgressChanged & Delegate) override |
| virtual void | **[[UnbindOnTimedQuestStatusChanged]]**(const FOnTimedQuestStatusChanged & Delegate) override |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FString | **[[BackendId]]**  |
| FTimespan return | **[[FTimespan]]**  |
| void void void TSoftObjectPtr< UTexture2D > return | **[[NULL]]**  |
| TSoftObjectPtr< UTexture2D > return | **[[NULL]]**  |
| void void void bool return | **[[false]]**  |
| void void void bool return | **[[false]]**  |
| float | **[[return]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200