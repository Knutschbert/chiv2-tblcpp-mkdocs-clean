---
title: UAchievementsList
type: class
aliases: UAchievementsList
share: false

---

# UAchievementsList





Inherits from UWidget

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam]]**(UWidget * , FOnGenerateAchievement , const [FAchievementProgress](/docs/SDK/Source/Classes/structFAchievementProgress.md) & , Achievement ) |
| | **[[DECLARE_DYNAMIC_DELEGATE_RetVal_OneParam]]**(bool , FOnFilterAchievement , const [FAchievementProgress](/docs/SDK/Source/Classes/structFAchievementProgress.md) & , Achievement ) |
| | **[[DECLARE_DYNAMIC_DELEGATE_RetVal_TwoParams]]**(bool , FOnSortAchievement , const [FAchievementProgress](/docs/SDK/Source/Classes/structFAchievementProgress.md) & , A , const [FAchievementProgress](/docs/SDK/Source/Classes/structFAchievementProgress.md) & , B ) |
| [FAchievementProgress](/docs/SDK/Source/Classes/structFAchievementProgress.md) | **[[GetProcessedItemAt]]**(int32 Index) |
| int32 | **[[GetProcessedItemsCount]]**() |
| void | **[[Initialize]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * InPlayerState) |
| | **[[UAchievementsList]]**() |
| void | **[[UpdateProcessedItems]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FOnFilterAchievement | **[[OnFilterAchievementEvent]]**  |
| FOnGenerateAchievement | **[[OnGenerateAchievementEvent]]**  |
| FOnSortAchievement | **[[OnSortAchievementEvent]]**  |
| [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * | **[[PlayerState]]**  |
| FName | **[[TableRowStyleName]]**  |
| TArray< [UAchievementInstance](/docs/SDK/Source/Classes/classUAchievementInstance.md) * > | **[[TrackedObjects]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200