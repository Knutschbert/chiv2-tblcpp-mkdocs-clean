---
title: UQuestPool
type: class
aliases: UQuestPool
share: false

---

# UQuestPool





Inherits from UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AbandonQuest]]**(TScriptInterface< [IQuest](/docs/SDK/Source/Classes/classIQuest.md) > Quest) |
| TArray< TScriptInterface< [IQuest](/docs/SDK/Source/Classes/classIQuest.md) > > | **[[GetActiveQuests]]**() |
| TArray< TScriptInterface< [IQuest](/docs/SDK/Source/Classes/classIQuest.md) > > | **[[GetDailyQuests]]**() |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| int32 | **[[GetMaxActiveQuests]]**() |
| TArray< TScriptInterface< [IQuest](/docs/SDK/Source/Classes/classIQuest.md) > > | **[[GetWeeklyQuests]]**() |
| void | **[[SlotQuest]]**(TScriptInterface< [IQuest](/docs/SDK/Source/Classes/classIQuest.md) > Quest) |
| | **[[UQuestPool]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FOnQuestsChanged | **[[OnQuestsChanged]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200