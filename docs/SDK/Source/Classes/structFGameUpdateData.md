---
title: FGameUpdateData
type: struct
aliases: FGameUpdateData
share: false

---

# FGameUpdateData





Inherits from FTableRowBase

## Public Functions

|                | Name           |
| -------------- | -------------- |
| TBL_API | **[[FGameUpdateData]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TSoftClassPtr< [UTBLGameUpdateContentWidget](/docs/SDK/Source/Classes/classUTBLGameUpdateContentWidget.md) > | **[[ContentWidgetClass]]**  |
| TSoftObjectPtr< UTexture2D > | **[[NewsThumbnail]]**  |
| FDateTime | **[[ReleaseDate]]**  |
| TArray< [FGameUpdateScheduleEntry](/docs/SDK/Source/Classes/structFGameUpdateScheduleEntry.md) > | **[[ShowSchedule]]**  |
| TSoftObjectPtr< UTexture2D > | **[[Thumbnail]]**  |
| FText | **[[Title]]**  |
| EGameUpdateType | **[[UpdateType]]**  |
| FString | **[[VersionNumber]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200