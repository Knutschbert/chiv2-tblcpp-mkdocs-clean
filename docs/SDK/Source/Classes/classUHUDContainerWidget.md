---
title: UHUDContainerWidget
type: class
aliases: UHUDContainerWidget
share: false

---

# UHUDContainerWidget





Inherits from [UTBLUserWidget](/docs/SDK/Source/Classes/classUTBLUserWidget.md), UUserWidget

Inherited by [UHUDCrosshairContainerWidget](/docs/SDK/Source/Classes/classUHUDCrosshairContainerWidget.md), [UHUDMarkerContainerWidget](/docs/SDK/Source/Classes/classUHUDMarkerContainerWidget.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AddSubwidget]]**([UHUDContainerSubWidget](/docs/SDK/Source/Classes/classUHUDContainerSubWidget.md) * SubWidget) |
| void | **[[ManuallyUpdate]]**() |
| void | **[[PopulateWidgetPool]]**() |
| void | **[[RemoveSubwidget]]**([UHUDContainerSubWidget](/docs/SDK/Source/Classes/classUHUDContainerSubWidget.md) * SubWidget) |
| void | **[[SubwidgetInitFromPool]]**([UHUDContainerSubWidget](/docs/SDK/Source/Classes/classUHUDContainerSubWidget.md) * SubWidget) |
| void | **[[SubwidgetReturnToPool]]**([UHUDContainerSubWidget](/docs/SDK/Source/Classes/classUHUDContainerSubWidget.md) * SubWidget) |
| | **[[UHUDContainerWidget]]**() |
| void | **[[Update]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TSet< [UHUDContainerSubWidget](/docs/SDK/Source/Classes/classUHUDContainerSubWidget.md) * > | **[[AllActiveWidgets]]**  |
| TSet< UClass * > | **[[LoadedSubWidgetClasses]]**  |
| TMap< UActorComponent *, [FWrappedStreamableHandle](/docs/SDK/Source/Classes/structFWrappedStreamableHandle.md) > | **[[PendingWidgets]]**  |
| TMap< UClass *, [FHudContainerPoolEntry](/docs/SDK/Source/Classes/structFHudContainerPoolEntry.md) > | **[[Pool]]**  |
| TArray< [FHUDContainerPoolInfo](/docs/SDK/Source/Classes/structFHUDContainerPoolInfo.md) > | **[[PooledWidgets]]**  |
| EWidgetContainer | **[[WidgetContainerType]]**  |
| TMap< UActorComponent *, [UHUDContainerSubWidget](/docs/SDK/Source/Classes/classUHUDContainerSubWidget.md) * > | **[[Widgets]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200