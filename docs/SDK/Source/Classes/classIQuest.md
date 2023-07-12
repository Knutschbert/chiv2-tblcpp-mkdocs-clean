---
title: IQuest
type: class
aliases: IQuest
share: false

---

# IQuest





Inherits from IInterface

Inherited by [UAchievementQuest](/docs/SDK/Source/Classes/classUAchievementQuest.md), [UCampaignImpl](/docs/SDK/Source/Classes/classUCampaignImpl.md), [UCampaignStub](/docs/SDK/Source/Classes/classUCampaignStub.md), [UQuestStub](/docs/SDK/Source/Classes/classUQuestStub.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void virtual void virtual void | **[[BindOnCompleted]]**(const FOnQuestCompleteChanged & Delegate) |
| virtual void virtual void | **[[BindOnProgressChanged]]**(const FOnQuestProgressChanged & Delegate) |
| virtual void | **[[BindOnTimedQuestStatusChanged]]**(const FOnTimedQuestStatusChanged & Delegate) |
| virtual float | **[[GetProgress]]**() const |
| virtual TArray< [FQuestReward](/docs/SDK/Source/Classes/structFQuestReward.md) > | **[[GetRewards]]**() const |
| virtual FTimespan | **[[GetTimeRemaining]]**() const |
| virtual bool | **[[IsClientAuthoritative]]**() const |
| virtual bool | **[[IsComplete]]**() const |
| virtual bool | **[[IsExpired]]**() const |
| virtual bool | **[[IsTimeAvailable]]**() const |
| virtual bool | **[[IsTimed]]**() const |
| virtual void virtual void virtual void virtual bool | **[[IsUpcoming]]**() const |
| TArray< [FQuestReward](/docs/SDK/Source/Classes/structFQuestReward.md) > return | **[[TArray]]**() |
| virtual void virtual void virtual void | **[[UnbindOnCompleted]]**(const FOnQuestCompleteChanged & Delegate) |
| virtual void virtual void | **[[UnbindOnProgressChanged]]**(const FOnQuestProgressChanged & Delegate) |
| virtual void | **[[UnbindOnTimedQuestStatusChanged]]**(const FOnTimedQuestStatusChanged & Delegate) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FTimespan return | **[[FTimespan]]**  |
| void virtual void virtual void virtual bool return | **[[false]]**  |
| bool return | **[[false]]**  |
| float | **[[return]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200