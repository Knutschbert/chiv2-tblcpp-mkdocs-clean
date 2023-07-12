---
title: FMarkedActorEntry
type: struct
aliases: FMarkedActorEntry
share: false

---

# FMarkedActorEntry





Inherited by [FMarkedActorEntryAmmoRefill](/docs/SDK/Source/Classes/structFMarkedActorEntryAmmoRefill.md), [FMarkedActorEntryBurnable](/docs/SDK/Source/Classes/structFMarkedActorEntryBurnable.md), [FMarkedActorEntryInteractable](/docs/SDK/Source/Classes/structFMarkedActorEntryInteractable.md), [FMarkedActorEntryStatsComponent](/docs/SDK/Source/Classes/structFMarkedActorEntryStatsComponent.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| TBL_API | **[[FMarkedActorEntry]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< UPrimitiveComponent * > | **[[CollsionComponents]]**  |
| TWeakObjectPtr< [UHudMarkerDisplayComponent](/docs/SDK/Source/Classes/classUHudMarkerDisplayComponent.md) > | **[[HUDMarkerComponent]]**  |
| TWeakObjectPtr< AActor > | **[[MarkedActor]]**  |
| TWeakObjectPtr< [UWidgetVisibilityComponent](/docs/SDK/Source/Classes/classUWidgetVisibilityComponent.md) > | **[[VisibilityComponent]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200