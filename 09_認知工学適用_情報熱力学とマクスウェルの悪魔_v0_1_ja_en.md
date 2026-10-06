# 認知工学適用：情報熱力学とマクスウェルの悪魔
## ― 「情報」を物理実体へ昇格させないための系境界・相関・記述ラベル監査 ―

**版**：v0.1  
**改訂日**：2026-10-07  
**著者**：がっちむち♂  
**文章生成支援**：LLM  
**原典言語**：日本語  

> **翻訳階層規定**：Part I = J0 日本語正本。Part II = T2 / English Summary Projection。T2は全文翻訳ではなく、独立した正本・規定文書ではない。意味衝突・欠落・曖昧さ・翻訳残差がある場合はJ0を優先し、下流側で新規主張を補わない。詳細は `TRANSLATION_POLICY.md`。

> **位置づけ**：本稿は熱力学・統計力学の数式や実験結果そのものを否定する論文ではない。認知工学から、対象・系境界・状態・相関・測定・記録・制御・「情報」という語の成立順序を監査する。

> **成立判定**：本稿の定義では、情報を自然界に独立して存在する物理実体として置く根拠が示されない限り、**情報熱力学は独立した自然科学としては成立しない**。ただし、そこで得られる有効な数式・実験・制御結果まで無効になるとはしない。

---

# 1. 問題設定

情報熱力学では、マクスウェルの悪魔、測定、フィードバック、メモリ、消去、相互情報量、仕事、熱、自由エネルギー等が一つの理論語彙で扱われる。

標準的な文献は、マクスウェルの悪魔を思考実験として扱い、Landauer原理、相互情報量、非平衡統計力学等を通じて情報処理と熱力学量の関係を記述する。

本稿が問うのは、その数式が使えるかではない。

> **「情報」と呼んだものは、物理系の側に独立して存在したのか。それとも観測者が状態差・相関・利用可能性へ与えた記述ラベルなのか。**

ここを分ける。

---

# 2. 認知工学からの分解

物理的な装置を完全に閉じるなら、少なくとも次が存在する。

- 物理系
- 粒子・状態
- 相互作用
- センサー
- メモリ媒体
- 制御器
- アクチュエータ
- 電源
- リセット過程
- 熱
- 仕事
- エネルギー移動
- 相関
- 時間発展

これらは物理状態・物理過程として観測可能である。

一方、

- これは1 bitである
- これは情報を得た
- これは情報を消去した
- これは情報を仕事へ変換した

という記述は、物理状態の差異・相関・機能を、観測者が特定の記述体系で分類した後に成立する。

したがって、

```text
物理状態
→ 差異の観測
→ 系分割
→ 状態分類
→ 相関の記述
→ 機能的利用
→ 「情報」というラベル
```

という成立順序を監査する必要がある。

---

# 3. マクスウェルの悪魔という「虚構」

本稿で「虚構の悪魔」と呼ぶのは、マクスウェルの悪魔が詐欺的・無価値という意味ではない。

> **悪魔は、系境界・測定・記録・制御・選別を一つの擬人化された主体へ圧縮した思考実験上の構成物である。**

という意味である。

悪魔を、

```text
観測する者
記録する者
判断する者
扉を操作する者
```

として置くと、「悪魔が情報を得た」という記述が自然に見える。

しかし、デーモン装置を、

```text
センサー
+ 物理メモリ
+ 制御
+ アクチュエータ
+ 電源
+ リセット
+ 被制御系
```

まで含めて閉じれば、残るのは物理状態・相関・制御・相互作用・エネルギー移動である。

したがって、

> **悪魔を追加したことで新しい自然現象が増えたのではなく、既存の物理過程を情報語彙で再記述した可能性を先に監査する。**

---

# 4. Landauer原理の位置

Landauer原理は、論理的に不可逆な操作を物理媒体で実装するときの熱力学的制約を扱う。

本稿はこの物理的制約を否定しない。

しかし、

```text
情報消去の物理実装に熱力学コストがある
```

ことから、

```text
情報それ自体が独立した物理実体である
```

を自動的には導かない。

媒体の状態変更に物理コストがあることと、その状態差へ「情報」という認知ラベルを与えたことは分ける。

> **Landauer原理は物理操作の制約であって、情報という存在物をエネルギーへ変換する存在論的な橋ではない。**

---

# 5. 「情報から仕事へ」の分解

情報熱力学では、相互情報量と抽出可能仕事の関係等が記述される。

認知工学からは、これを次のように分解する。

```text
物理状態間に相関がある
↓
観測者がその相関を区別・記録できる
↓
制御操作が相関を利用する
↓
通常なら取り出せない条件から仕事を抽出する
↓
その有効相関を「情報」と呼ぶ
```

したがって、

```text
information → work
```

を、独立した情報物質が仕事へ変換されたという存在論へ読まない。

本稿では、

> **相関を利用できる物理系から仕事が抽出された**

という物理記述と、

> **その相関を情報と呼んだ**

という記述操作を分離する。

---

# 6. 情報熱力学の成立判定

もし情報が、

> **物理状態・差異・相関・関係を、観測者が目的・分類・利用可能性に応じて切り出した記述量**

であるなら、情報熱力学が扱う有効部分は、

- 統計力学
- 非平衡熱力学
- 確率過程
- 制御
- 測定
- 相関
- 物理メモリ

の組合せとして再記述できる。

その場合、

> **「情報熱力学」という名称は有用な横断ラベルとしては成立しても、情報という独立自然物を対象とする独立自然科学としては成立しない。**

これが本稿の認知工学上の成立判定である。

---

# 7. 何を否定していないか

本稿は次を否定しない。

- 第二法則
- 統計力学
- 非平衡過程
- Landauer原理の物理的検証
- 相互情報量を用いた有効な数理記述
- フィードバック制御
- 実験で観測された仕事・熱・確率分布

否定しているのは、

> **これらが成功したことを根拠に、「情報」が認知から独立した自然物として実在すると昇格する認知操作**

である。

---

# 8. 神の領域原理（仮）との関係

```text
物理状態
≠
物理状態について作った情報記述
```

である。

認知後に成立した「情報」「bit」「相関資源」「情報から仕事へ」という世界像を、認知以前の世界本体にそのまま存在する構成物へ昇格させない。

---

# 9. 反証・再開放条件

本稿は少なくとも次の場合に再監査する。

- 「情報」が観測者による系分割・状態分類・意味づけに依存せず、一意な独立物理量として同定された
- 情報という存在論を導入しなければ説明できない物理効果が示され、通常の物理状態・相関・制御記述では同型再構成できない
- 本稿の系境界閉包が既存実験の重要な観測量を欠落させる
- 「情報」と「物理相関」を分けること自体が観測上破綻する

---

# 10. 結論

本稿の核心は単純である。

> **情報を使って物理を記述できることと、情報が独立した物理実体であることは別である。**

マクスウェルの悪魔を完全な物理装置として閉じれば、センサー、メモリ、制御、相関、エネルギー移動、リセット等の通常の物理過程が残る。

したがって認知工学からは、まず物理過程を閉じ、その後に「情報」というラベルが何を圧縮しているかを監査する。

---

# Part II. English Summary Projection

# Cognitive-Engineering Audit of Information Thermodynamics and Maxwell's Demon

**Version**: v0.1  
**Revision date**: 2026-10-07  
**Author**: がっちむち♂  
**Writing assistance**: LLM  
**Authoritative language**: Japanese



**Translation class**: T2 / English Summary Projection  
**Source authority**: Japanese Part I / J0  
**Translation status**: CURRENT  
**Authority**: Non-authoritative and non-exhaustive. It may omit detail and must not add normative claims. In conflict, ambiguity, omission, or translation residual, Japanese Part I prevails.  
**Policy**: `TRANSLATION_POLICY.md`This paper does not reject thermodynamics, statistical mechanics, Landauer-type physical constraints, or experimentally observed work and heat. It audits the step by which physical states, distinctions, correlations, memory states, and control relations are relabeled as “information” and then promoted into an independent physical ontology.

Maxwell's demon is treated as a thought-experiment compression of sensing, memory, control, actuation, power, reset, and the controlled system. Once the full physical system is closed, ordinary physical states, correlations, interactions, and energy flows remain.

The paper therefore separates:

```text
physical correlation used for control
from
the observer's description of that correlation as information
```

Landauer's principle constrains physical implementations of logically irreversible operations; it does not by itself establish information as a separate physical substance.

Under this cognitive-engineering framework, “information thermodynamics” may remain a useful interdisciplinary label, but it does not constitute an independent natural science whose primitive object is an observer-independent entity called information unless such an entity is separately established.

## Orientation references

- Parrondo, Horowitz & Sagawa (2015), *Thermodynamics of information*, Nature Physics.
- Georgescu (2021), *60 years of Landauer's principle*, Nature Reviews Physics.
