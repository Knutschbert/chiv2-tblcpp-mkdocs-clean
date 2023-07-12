---
title: UOnlineConfig
type: class
aliases: UOnlineConfig
share: false

---

# UOnlineConfig





Inherits from UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[EventGetAchievementCategory]]**(const [FAchievementProgress](/docs/SDK/Source/Classes/structFAchievementProgress.md) & InAchievement, FText & Category, FText & Subcategory, int32 & DisplayPriority) |
| [FTitleProgressionRow](/docs/SDK/Source/Classes/structFTitleProgressionRow.md) | **[[GetTitleProgression]]**(int32 Level) |
| | **[[UOnlineConfig]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< TEnumAsByte< EGameModeType::Type > > | **[[GameModeWinAchievements]]**  |
| TArray< [FLevelSet](/docs/SDK/Source/Classes/structFLevelSet.md) > | **[[LevelWinAchievements]]**  |
| UDataTable * | **[[TitleProgressionTable]]**  |
| TArray< EInventoryType > | **[[WeaponAchievements]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200