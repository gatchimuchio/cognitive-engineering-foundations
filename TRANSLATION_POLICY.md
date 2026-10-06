# 日本語基底・翻訳階層・翻訳制度
## Translation Hierarchy and Governance Policy

**版**：v1.4  
**改訂日**：2026-10-07  
**著者**：がっちむち♂  
**規定言語**：日本語  

本書は `cognitive-engineering-foundations` における翻訳・要約射影・解説射影・作業翻訳の上下関係、権限、更新、検証、残差管理を規定する。

> **最上位原則：意味の正本は日本語に置く。翻訳・要約・解説は、日本語正本から派生する下流Projectionであり、日本語正本を上書きしない。**

---

# 1. 翻訳ヒエラルキー

本体系の言語階層を次の5段階に固定する。

```text
J0  Japanese Canonical Original
    日本語正本
        ↓
T1  Aligned Full Translation
    節対応全文翻訳
        ↓
T2  Summary Projection
    要約射影
        ↓
T3  Explanatory Projection
    解説射影
        ↓
W   Working Translation
    作業翻訳
```

下流へ行くほど、意味上の権限は小さくなる。

```text
Authority(J0) > Authority(T1) > Authority(T2) > Authority(T3) > Authority(W)
```

ただし、T1以下はいずれも**正本ではない**。

---

# 2. J0：日本語正本

J0は、本体系において唯一の規定言語・意味上の正本である。

J0では、

- 定義
- 主張
- 否定
- 条件
- 例外
- 因果
- 階層
- 射程
- 禁止
- 留保
- SUSPEND
- 再開放条件
- 用語間の関係

を確定する。

翻訳上の読みやすさ、英語圏の慣用表現、既存学術語彙との整合のために、J0の意味を変更してはならない。

> **他言語へ訳しにくいことは、日本語正本を英語へ合わせて削る理由にならない。**

---

# 3. T1：節対応全文翻訳

T1だけを、本制度上 `Translation` と呼ぶ。

T1は、日本語正本の全節を対象に、可能な限り意味・関係・否定・条件・順序を対応させた全文翻訳である。

T1は少なくとも次を満たす。

1. 日本語正本の全節を対象とする。
2. 節の省略を原則として行わない。
3. 新しい主張・根拠・例外・因果・規範を追加しない。
4. 否定、条件、量化、留保、強度を保持する。
5. 用語ロックに従う。
6. 訳し切れない残差を隠さない。
7. 出典となる日本語版・版番号を明示する。

T1は引用補助・国際共有に利用できるが、意味衝突時の最終裁定権は持たない。

```text
T1 conflicts with J0
→ J0 wins
```

---

# 4. T2：要約射影

T2は `Summary Projection` であり、**Translationではない**。

T2は、日本語正本から主要な意味構造・主張・境界を抽出し、短く再構成した下流Projectionである。

許可されること：

- 節の省略
- 重複の圧縮
- 読書順の簡略化
- 代表例への集約

禁止されること：

- 日本語正本にない新主張の追加
- 日本語正本より強い断定
- 日本語正本より弱い断定への無断変更
- 因果方向・上下関係・禁止境界の変更
- 要約を全文翻訳と表示すること

現行root番号付き正本群の英語部はすべてT2として扱う。

---

# 5. T3：解説射影

T3は `Explanatory Projection` である。

T3は、特定読者向けに、

- 比喩
- 例
- FAQ
- 図解
- 既存学問との比較
- 読み替え
- 教育的順序変更

等を用いて説明するための層である。

T3は最も読みやすくできる一方、原典との逐語対応を保証しない。

したがって、

> **T3を理論定義・適合判定・反証判定の根拠として使用してはならない。**

---

# 6. W：作業翻訳

Wは未監査の作業翻訳である。

LLM翻訳、機械翻訳、人間による初稿、対訳途中版等を含む。

Wは、

- 公開正本ではない
- 引用基準ではない
- 適合判定に使用しない
- J0/T1/T2/T3として表示しない

とする。

Wから直接J0を書き換えない。

---

# 7. 翻訳逆流禁止

翻訳・要約・解説の途中で、日本語正本の、

- 曖昧さ
- 未定義語
- 矛盾
- 関係欠落
- 説明不足
- 誤り候補

を発見した場合、下流側で勝手に補完・修正しない。

必ず、

```text
翻訳側で問題発見
→ J0へ差し戻し
→ 日本語で監査
→ 必要なら日本語版を改訂
→ 版を更新
→ T1/T2/T3を再生成
```

とする。

> **下流Projectionが上流の意味を黙って修理してはならない。**

---

# 8. 翻訳状態

各翻訳・射影は、次の状態を持つ。

- **CURRENT**：対応する日本語正本と同期済み
- **STALE**：日本語正本が更新されたが、下流版が未同期
- **HOLD**：意味残差・未解決衝突があり公開適合を保留
- **RETIRED**：旧版として履歴保存

日本語正本の意味が変わる版更新があった時点で、既存T1/T2/T3は自動的にCURRENTではなくなる。

再監査後にのみCURRENTへ戻す。

---

# 9. 必須メタデータ

T1/T2/T3は、可能な限り次を明示する。

```text
Source authority: Japanese Canonical Original (J0)
Source version: <version>
Translation class: T1 / T2 / T3
Translation status: CURRENT / STALE / HOLD / RETIRED
Target language: <language>
Authority: Non-authoritative
```

T1ではさらに、

- 翻訳版番号
- 節対応範囲
- 未解決残差
- 用語対応

を保持する。

---

# 10. 用語ロック

翻訳は、既存の英単語へ概念を押し込むことで意味を変えてはならない。

特に次をロックする。

| 日本語正本 | 英語側の扱い |
|---|---|
| 神の領域原理（仮） | 正式名は日本語を保持。説明上 `Shiniki Principle` を併記可 |
| 神域原理（仮） | 日本語略称を保持 |
| トリニティ原理 | `Trinity Principle` |
| 閉包位相Ψ | `Closure Phase Ψ` |
| 意識論 | `Theory of Consciousness` |
| 認知工学 | `Cognitive Engineering` |
| 人間意思決定理論（仮） | 日本語名を保持。HDSとの対応を明示 |
| HDS | `HDS` |
| （仮） | 原則として削除しない |
| Projection | 本体系の意味では安易に `model` / `representation` へ置換しない |

「粋」「野暮」「間」等、英語一語で意味同型を保証できない語は、日本語を保持し、必要に応じて説明を併記する。

---

# 11. 翻訳残差

日本語から他言語へ完全同型に回収できない意味を、**翻訳残差**として扱う。

翻訳残差は失敗ではない。

重要なのは、

> **残差を消したふりをしないこと。**

意味差が重要な場合、

```text
Japanese term: <原語>
Approximate rendering: <訳語>
Residual: <失われる意味・関係・含意>
```

として保持する。

翻訳しないことが、最も忠実な翻訳操作になる場合を認める。

---

# 12. 翻訳監査ゲート

T1/T2/T3の公開前に、必要な範囲で次を監査する。

## G-T1 Source Gate
対応する日本語正本・版が一意に特定されているか。

## G-T2 Terminology Gate
固定語の訳語・非翻訳方針が守られているか。

## G-T3 Relation Gate
上下関係、因果方向、依存、包含、非同一性が変わっていないか。

## G-T4 Polarity / Modality Gate
否定、禁止、留保、`〜ではない`、`〜し得る`、`必ず` 等の強度が変わっていないか。

## G-T5 Scope Gate
射程・条件・時点・対象範囲が拡大／縮小されていないか。

## G-T6 Residual Gate
訳し切れない意味が隠蔽されていないか。

## G-T7 Addition Gate
日本語正本に存在しない新主張が混入していないか。

## G-T8 Status Gate
CURRENT / STALE / HOLD等の状態表示が正しいか。

---

# 13. 引用・適合・反証時の優先順位

厳密な意味争い、理論適合性、反証、用語定義では、

```text
J0を参照する
```

を原則とする。

T1はJ0を読むための高忠実度補助資料。

T2は主要構造を把握するための要約。

T3は理解補助。

Wは作業物。

したがって、

```text
T2/T3の文言だけを根拠に
J0の主張を反証・変更・適合判定してはならない。
```

---

# 14. ファイル配置

現在の番号付きroot文書は、

```text
Part I  = J0 日本語正本
Part II = T2 English Summary Projection
```

という複合文書として運用する。

ファイル名の `_ja_en.md` は「日本語正本と英語下流部を同居させる」ことを示すだけで、英語部がT1全文翻訳であることを意味しない。

T1全文翻訳は番号付き正本へ混在させず、

```text
translations/<language>/full/
```

へ独立配置する。

2026-10-07時点では、現行番号付き正本群00〜12＋05Aの全14本について、

```text
translations/en/full/
```

に英語T1全文翻訳を配置済みであり、全て `CURRENT` とする。

対応関係・CURRENT状態・節番号整合監査は `translations/en/full/README.md` を正とする。

T3は、

```text
translations/<language>/explanatory/
```

等の下流領域へ分離する。

---

# 15. 現行英語部の判定

2026-10-07時点のroot番号付き正本群（00〜12および05A）について、

> **root内Part IIの英語部はすべてT2 / English Summary Projectionである。**

同時に、その全14本に対応する、

> **T1 / Aligned Full Translation は `translations/en/full/` に全て存在し、CURRENTである。**

したがって、

```text
短い入口・概略把握 = T2
英語で本文全体を読む = T1
意味の最終裁定 = J0
```

と使い分ける。

J0の意味を変更する版更新が発生した時点で、対応するT1/T2は自動的にCURRENTではなくなり、再監査後にのみCURRENTへ戻す。

README、PUBLICATION_POLICY、REFERENCES等の英語要約部も、全文対応を満たさない限り `English Translation` と表示しない。

---

# 16. 自己適用

本翻訳制度自体も、日本語で記述された現在Projectionである。

「日本語正本」という制度を、民族・人種・言語話者の優劣へ変換してはならない。

日本語を正本とする理由は、本体系が日本語で生成・分別・監査されてきたという**成立系譜と意味保持の設計上の理由**である。

将来、別言語・別表現系に日本語正本と同等以上の意味保持が成立したと主張する場合、その同等性自体を別途監査する。

---

# Part II. English Summary Projection

# Translation Hierarchy and Governance Policy

**Translation class**: T2 / English Summary Projection  
**Source authority**: Japanese Canonical Original (J0)  
**Translation status**: CURRENT  
**Authority**: Non-authoritative and non-exhaustive

The Japanese original is the sole normative source. Downstream language products are ordered as:

```text
J0 Japanese Canonical Original
> T1 Aligned Full Translation
> T2 Summary Projection
> T3 Explanatory Projection
> W Working Translation
```

Only T1 is called a Translation in the strict policy sense. T2 and T3 are Projections and must not be presented as full translations.

If translation reveals ambiguity, contradiction, missing definitions, or other defects, the downstream text must not silently repair them. The issue is returned to J0, resolved in Japanese, versioned there, and only then propagated downstream.

Core terminology is locked. Terms without an isomorphic rendering may retain the Japanese original with an explanatory gloss and an explicit translation residual.

Every downstream layer is non-authoritative. In any semantic conflict, the Japanese Canonical Original controls.
