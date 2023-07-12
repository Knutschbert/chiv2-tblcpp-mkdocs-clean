---
title: FActionContext
type: struct
aliases: FActionContext
share: false

---

# FActionContext





## Public Functions

|                | Name           |
| -------------- | -------------- |
| TBL_API | **[[FActionContext]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * | **[[AbilitySpec]]**  |
| TWeakObjectPtr< AActor > | **[[CharacterWhoParried]]**  |
| TWeakObjectPtr< UPrimitiveComponent > | **[[CollisionComponent]]**  |
| FVector | **[[HitDirection]]**  |
| FHitResult | **[[HitResult]]**  |
| FVector | **[[ImpactPointOverride]]**  |
| TWeakObjectPtr< [AAbilityInvocation](/docs/SDK/Source/Classes/classAAbilityInvocation.md) > | **[[Invocation]]**  |
| TWeakObjectPtr< AActor > | **[[Projectile]]**  |
| TWeakObjectPtr< [UAbilityTargetMethod](/docs/SDK/Source/Classes/classUAbilityTargetMethod.md) > | **[[TargetMethod]]**  |
| TWeakObjectPtr< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[Weapon]]**  |
| bool | **[[bArrowParried]]**  |
| bool | **[[bCosmetic]]**  |
| bool | **[[bDisarmed]]**  |
| bool | **[[bHeadShotDamageOnly]]**  |
| bool | **[[bIgnoreAutonomousActions]]**  |
| bool | **[[bIsInTeamThwackRange]]**  |
| bool | **[[bMultiAttackHitParry]]**  |
| bool | **[[bOverrideImpactPoint]]**  |
| bool | **[[bParried]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200