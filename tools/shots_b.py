# -*- coding: utf-8 -*-
"""分镜 2-3 ~ 3-3"""

S23 = {
    "id": "2-3",
    "title": "两张报表合起来怎么读",
    "bg": "#f3ead9", "ink": "#1b2340", "accent": "#ff3d7f", "muted": "#6b6a74",
    "font": '"PingFang SC","Microsoft YaHei",sans-serif',
    "sub": "Risograph 双色套印 · 三步读法",
    "css": """
.riso{position:absolute;inset:0;background:#f3ead9}
.riso:before{content:"";position:absolute;inset:0;opacity:.16;background-image:
  radial-gradient(#1b2340 1px, transparent 1.6px);background-size:14px 14px}
.riso:after{content:"";position:absolute;inset:0;opacity:.12;background-image:
  radial-gradient(#ff3d7f 1px, transparent 1.6px);background-size:14px 14px;background-position:7px 7px}
.kick{position:absolute;left:96px;top:82px;font:700 20px/1 Consolas,monospace;letter-spacing:.42em;color:#ff3d7f}
.h1{position:absolute;left:92px;top:120px;font:800 74px/1.1 "PingFang SC","Microsoft YaHei",sans-serif;color:#1b2340}
.h1 em{font-style:normal;color:#ff3d7f}
.steps{position:absolute;left:92px;right:92px;top:320px;display:flex;gap:34px}
.step{flex:1;position:relative;padding:30px 28px;background:#fbf5e8;border:3px solid #1b2340;
  box-shadow:12px 12px 0 rgba(255,61,127,.9)}
.step .no{font:900 72px/1 Impact,"Arial Black",sans-serif;color:#ff3d7f;letter-spacing:-.02em}
.step h3{margin:10px 0 12px;font:800 31px/1.3 "PingFang SC",sans-serif;color:#1b2340}
.step p{font:400 19px/1.8 "PingFang SC",sans-serif;color:#3a3f57}
.step .tag{position:absolute;right:22px;top:22px;font:700 15px/1 Consolas,monospace;color:#1b2340;opacity:.5}
.band{position:absolute;left:0;right:0;bottom:0;height:150px;background:#1b2340}
.band .t{position:absolute;left:96px;top:44px;font:700 30px/1.4 "PingFang SC",sans-serif;color:#f3ead9}
.band .t em{font-style:normal;color:#ff3d7f}
.band .r{position:absolute;right:96px;top:52px;font:500 16px/1 Consolas,monospace;color:#8e94ad;letter-spacing:.16em}
""",
    "body": """
<div class="riso">
  <div class="kick fx" id="e1">TWO STATEMENTS · HOW TO READ</div>
  <div class="h1 fx d1" id="e2">两张报表<br><em>合起来</em>怎么读</div>
  <div class="steps">
    <div class="step fx d2" id="e3"><div class="tag">01</div><div class="no">01</div>
      <h3>先看结构</h3><p>资产 = 负债 + 权益。谁的负债是「借来的」、谁是「预收来的」，决定风险的性质。</p></div>
    <div class="step fx d2" id="e4"><div class="tag">02</div><div class="no">02</div>
      <h3>再看利润</h3><p>营业收入 − 营业成本 − 期间费用 = 营业利润。毛利率守住了，利润率未必守得住。</p></div>
    <div class="step fx d3" id="e5"><div class="tag">03</div><div class="no">03</div>
      <h3>最后对齐口径</h3><p>同一笔货款，发货算收入还是到终端算收入，会把 303 亿元在两年之间搬来搬去。</p></div>
  </div>
  <div class="band fx d3" id="e6">
    <div class="t">合起来看，才是<em>同一门生意</em>的两本账。</div>
    <div class="r">2024 / 2025 ANNUAL REPORTS</div>
  </div>
</div>
""",
    "cues": [
        {"t": 200, "sel": "#e1", "act": "on"},
        {"t": 500, "sel": "#e2", "act": "on"},
        {"t": 1200, "sel": "#e3", "act": "on"},
        {"t": 1650, "sel": "#e4", "act": "on"},
        {"t": 2100, "sel": "#e5", "act": "on"},
        {"t": 2900, "sel": "#e6", "act": "on"},
    ],
    "dur": 16,
}

S31 = {
    "id": "3-1",
    "title": "四大类十项比率：一张公式矩阵",
    "bg": "#05100c", "ink": "#7bf5b6", "accent": "#7bf5b6", "muted": "#3f7d5e",
    "font": 'Consolas,"Courier New",monospace',
    "sub": "数据矩阵终端 · 10 项比率",
    "css": """
.term{position:absolute;inset:0;background:
  radial-gradient(90% 80% at 50% 0%, #0a1f16 0%, #05100c 65%, #030a08 100%)}
.term:after{content:"";position:absolute;inset:0;opacity:.20;background-image:
  repeating-linear-gradient(0deg,rgba(123,245,182,.12) 0 1px,transparent 1px 3px)}
.win{position:absolute;left:70px;right:70px;top:58px;bottom:64px;border:1px solid rgba(123,245,182,.34);
  background:rgba(3,14,10,.72);box-shadow:0 0 90px rgba(123,245,182,.10)}
.topbar{position:absolute;left:0;right:0;top:0;height:40px;border-bottom:1px solid rgba(123,245,182,.24);
  display:flex;align-items:center;gap:9px;padding:0 16px}
.dot{width:11px;height:11px;border-radius:50%;background:#1f6349}
.topbar b{margin-left:14px;font:600 15px/1 Consolas,monospace;letter-spacing:.18em;color:#4f9d78}
.cmd{position:absolute;left:26px;top:56px;font:500 19px/1.8 Consolas,monospace;color:#8ff7c2}
.cmd i{color:#3f7d5e;font-style:normal}
.hd{position:absolute;left:26px;right:26px;top:102px;display:flex;font:600 15px/1 Consolas,monospace;
  color:#3f7d5e;letter-spacing:.12em;padding-bottom:8px;border-bottom:1px solid rgba(123,245,182,.18)}
.hd span:nth-child(1){flex:1}
.hd span:nth-child(n+2){width:190px;text-align:right}
.list{position:absolute;left:26px;right:26px;top:130px}
.line{display:flex;align-items:baseline;padding:9px 0;border-bottom:1px dashed rgba(123,245,182,.13);
  font:500 23px/1 Consolas,monospace}
.line b{flex:1;color:#cdfbe2}
.line u{text-decoration:none;width:190px;text-align:right;color:#7bf5b6}
.line s{text-decoration:none;width:190px;text-align:right;color:#ffb547}
.foot{position:absolute;left:26px;bottom:14px;font:500 15px/1 Consolas,monospace;color:#38745a;letter-spacing:.14em}
""",
    "body": """
<div class="term">
  <div class="win fx" id="f0">
    <div class="topbar"><span class="dot"></span><span class="dot"></span><span class="dot"></span>
      <b>ratio_matrix — 2025 — zsh</b></div>
    <div class="cmd">$ ratios --year 2025 --basis consolidated <i># 10 项 · 4 类</i></div>
    <div class="hd"><span>RATIO</span><span>MOUTAI</span><span>WULIANGYE</span></div>
    <div class="list">
      <div class="line fx" id="g1"><b>流动比率</b><u>5.09×</u><s>2.45×</s></div>
      <div class="line fx" id="g2"><b>速动比率</b><u>3.85×</u><s>2.15×</s></div>
      <div class="line fx" id="g3"><b>毛利率</b><u>91.18%</u><s>77.54%</s></div>
      <div class="line fx" id="g4"><b>营业利润率</b><u>68.00%</u><s>30.23%</s></div>
      <div class="line fx" id="g5"><b>净利率</b><u>48.76%</u><s>22.09%</s></div>
      <div class="line fx" id="g6"><b>资本回报率</b><u>46.29%</u><s>9.46%</s></div>
      <div class="line fx" id="g7"><b>资产负债比率</b><u>19.64%</u><s>55.49%</s></div>
      <div class="line fx" id="g8"><b>利息保障倍数</b><u>3,995×</u><s>428×</s></div>
      <div class="line fx" id="g9"><b>存货周转率</b><u>0.26</u><s>0.48</s></div>
      <div class="line fx" id="g10"><b>应收账款周转率</b><u>15,645</u><s>1,079</s></div>
    </div>
    <div class="foot">数据：2024 / 2025 年度报告（合并报表口径）</div>
  </div>
</div>
""",
    "cues": [
        {"t": 200, "sel": "#f0", "act": "on"},
        {"t": 700, "sel": "#g1", "act": "on"},
        {"t": 1030, "sel": "#g2", "act": "on"},
        {"t": 1360, "sel": "#g3", "act": "on"},
        {"t": 1690, "sel": "#g4", "act": "on"},
        {"t": 2020, "sel": "#g5", "act": "on"},
        {"t": 2350, "sel": "#g6", "act": "on"},
        {"t": 2680, "sel": "#g7", "act": "on"},
        {"t": 3010, "sel": "#g8", "act": "on"},
        {"t": 3340, "sel": "#g9", "act": "on"},
        {"t": 3670, "sel": "#g10", "act": "on"},
    ],
    "dur": 16,
}

S32 = {
    "id": "3-2",
    "title": "流动性：5.09× 与 2.45× 的水位差",
    "bg": "#04121c", "ink": "#e6f6ff", "accent": "#28c2ff", "muted": "#5b87a1",
    "font": '"PingFang SC","Microsoft YaHei",sans-serif',
    "sub": "深水水位仪表 · 流动比率",
    "css": """
.deep{position:absolute;inset:0;background:
  radial-gradient(100% 90% at 50% 110%, #0a3550 0%, #04121c 55%, #020a11 100%)}
.kick{position:absolute;left:96px;top:80px;font:700 20px/1 Consolas,monospace;letter-spacing:.4em;color:#28c2ff}
.h1{position:absolute;left:94px;top:118px;font:800 62px/1.15 "PingFang SC",sans-serif;color:#e6f6ff}
.h1 em{font-style:normal;color:#28c2ff}
.tanks{position:absolute;left:50%;margin-left:-520px;top:270px;width:1040px;height:560px;
  display:flex;gap:200px;justify-content:center}
.tank{position:relative;width:240px;height:500px;border:2px solid rgba(40,194,255,.45);
  border-radius:6px 6px 0 0;background:rgba(6,32,48,.55)}
.tank .water{position:absolute;left:0;bottom:0;width:100%;height:0;
  background:linear-gradient(180deg,#39d3ff 0%,#1173a8 55%,#0a4a6e 100%);opacity:.86}
.tank .glow{position:absolute;left:0;right:0;height:3px;bottom:0;background:#8ce8ff;opacity:.9;box-shadow:0 0 22px #39d3ff}
.tticks{position:absolute;left:-120px;top:0;bottom:0;width:112px}
.tticks span{position:absolute;right:0;font:500 15px/1 Consolas,monospace;color:#4d7d96;transform:translateY(-50%)}
.tticks span:after{content:"";position:absolute;left:100%;top:50%;width:14px;height:1px;background:rgba(40,194,255,.35)}
.tcap{position:absolute;left:50%;transform:translateX(-50%);bottom:-118px;text-align:center;width:420px}
.tcap b{display:block;font:900 72px/1 Impact,"Arial Black",sans-serif;color:#e6f6ff}
.tcap b i{font-style:normal;font-size:38px;color:#28c2ff}
.tcap span{display:block;margin-top:8px;font:600 21px/1.4 "PingFang SC",sans-serif;color:#9dbfd2}
.note{position:absolute;left:96px;bottom:92px;font:400 21px/1.9 "PingFang SC",sans-serif;color:#7fa6bb}
.note b{color:#28c2ff;font-family:Consolas,monospace}
.foot{position:absolute;right:96px;bottom:56px;font:400 15px/1 Consolas,monospace;color:#41697d;letter-spacing:.1em}
""",
    "body": """
<div class="deep">
  <div class="kick fx" id="h1c">CURRENT RATIO · 2025</div>
  <div class="h1 fx d1" id="h2">5.09× 与 <em>2.45×</em> 的水位差</div>
  <div class="tanks">
    <div class="tank">
      <div class="tticks"><span style="bottom:0">0</span><span style="bottom:25%">2×</span>
        <span style="bottom:50%">4×</span><span style="bottom:75%">6×</span></div>
      <div class="water" id="wa"></div><div class="glow" id="ga"></div>
      <div class="tcap fx d2" id="h3"><b>5.09<i>×</i></b><span>贵州茅台 · 流动资产 25,251,866 万元</span></div>
    </div>
    <div class="tank">
      <div class="tticks"><span style="bottom:0">0</span><span style="bottom:25%">2×</span>
        <span style="bottom:50%">4×</span><span style="bottom:75%">6×</span></div>
      <div class="water" id="wb"></div><div class="glow" id="gb"></div>
      <div class="tcap fx d3" id="h4"><b>2.45<i>×</i></b><span>五粮液 · 流动资产 16,475,156 万元</span></div>
    </div>
  </div>
  <div class="note fx d3" id="h5">同样是先款后货：茅台把钱留在账上，五粮液把钱变成了库存与预收。<br>
  分母（流动负债）：<b>496.10 亿 对 673.52 亿</b></div>
  <div class="foot fx d3" id="h6">数据：2025 年年度报告（合并报表口径）</div>
</div>
""",
    "cues": [
        {"t": 200, "sel": "#h1c", "act": "on"},
        {"t": 450, "sel": "#h2", "act": "on"},
        {"t": 900, "sel": "#h3", "act": "on"},
        {"t": 950, "sel": "#wa", "act": "h", "arg": 64},
        {"t": 1050, "sel": "#ga", "act": "h", "arg": 64},
        {"t": 2100, "sel": "#h4", "act": "on"},
        {"t": 2150, "sel": "#wb", "act": "h", "arg": 31},
        {"t": 2250, "sel": "#gb", "act": "h", "arg": 31},
        {"t": 3600, "sel": "#h5", "act": "on"},
        {"t": 4300, "sel": "#h6", "act": "on"},
    ],
    "dur": 18,
}

S33 = {
    "id": "3-3",
    "title": "盈利能力：四条线，两个世界",
    "bg": "#120b09", "ink": "#ffe9d6", "accent": "#ff6a1a", "muted": "#9c7a63",
    "font": '"PingFang SC","Microsoft YaHei",sans-serif',
    "sub": "熔炉渐变柱状 · 四项利润率",
    "css": """
.furnace{position:absolute;inset:0;background:
  radial-gradient(80% 70% at 50% 118%, #6b2404 0%, #2a0f06 42%, #120b09 72%, #0a0709 100%)}
.kick{position:absolute;left:96px;top:80px;font:700 20px/1 Consolas,monospace;letter-spacing:.4em;color:#ff6a1a}
.h1{position:absolute;left:94px;top:118px;font:800 58px/1.15 "PingFang SC",sans-serif;color:#ffe9d6}
.h1 em{font-style:normal;color:#ff6a1a}
.legend{position:absolute;right:110px;top:150px;text-align:right;
  font:600 18px/2 Consolas,monospace;color:#9c7a63;letter-spacing:.08em}
.legend i{display:inline-block;width:16px;height:16px;margin-right:10px;vertical-align:-2px}
.legend .sa{background:linear-gradient(180deg,#ffd166,#c2410c)}
.legend .sb{background:#5d3a2b}
.chart{position:absolute;left:110px;right:110px;bottom:210px;height:420px;display:flex;gap:74px;
  align-items:flex-end;border-bottom:2px solid rgba(255,106,26,.35)}
.grp{flex:1;position:relative;height:100%;display:flex;align-items:flex-end;justify-content:center;gap:12px}
.grp .gl{position:absolute;left:0;right:0;bottom:-54px;text-align:center;
  font:600 21px/1.4 "PingFang SC",sans-serif;color:#c9a48b}
.col{position:relative;width:74px;height:100%;display:flex;align-items:flex-end}
.fill{position:relative;width:100%;height:var(--h);border-radius:3px 3px 0 0}
.fill.a{background:linear-gradient(180deg,#ffd166 0%,#ff8c1a 55%,#c2410c 100%);
  box-shadow:0 0 28px rgba(255,140,26,.35)}
.fill.b{background:linear-gradient(180deg,#8a5a44 0%,#5d3a2b 60%,#3a2318 100%)}
.val{position:absolute;left:50%;top:-30px;transform:translateX(-50%);font:700 23px/1 Consolas,monospace;
  color:#ffe9d6;white-space:nowrap}
.note{position:absolute;left:110px;bottom:92px;font:400 22px/1.85 "PingFang SC",sans-serif;color:#b08a72}
.note b{color:#ff8c1a;font-family:Consolas,monospace}
.foot{position:absolute;right:110px;bottom:56px;font:400 15px/1 Consolas,monospace;color:#7a5a48;letter-spacing:.1em}
""",
    "body": """
<div class="furnace">
  <div class="kick fx" id="k1c">PROFITABILITY · 4 METRICS</div>
  <div class="h1 fx d1" id="k2c">四条线，<em>两个世界</em></div>
  <div class="legend fx d2" id="k3c"><div><i class="sa"></i>贵州茅台</div><div><i class="sb"></i>五粮液</div></div>
  <div class="chart fx" id="chc">
    <div class="grp">
      <div class="col"><div class="fill a" id="ba1" style="--h:91%"><div class="val" id="va1">0</div></div></div>
      <div class="col"><div class="fill b" id="bb1" style="--h:78%"><div class="val" id="vb1">0</div></div></div>
      <div class="gl">毛利率</div></div>
    <div class="grp">
      <div class="col"><div class="fill a" id="ba2" style="--h:68%"><div class="val" id="va2">0</div></div></div>
      <div class="col"><div class="fill b" id="bb2" style="--h:30%"><div class="val" id="vb2">0</div></div></div>
      <div class="gl">营业利润率</div></div>
    <div class="grp">
      <div class="col"><div class="fill a" id="ba3" style="--h:49%"><div class="val" id="va3">0</div></div></div>
      <div class="col"><div class="fill b" id="bb3" style="--h:22%"><div class="val" id="vb3">0</div></div></div>
      <div class="gl">净利率</div></div>
    <div class="grp">
      <div class="col"><div class="fill a" id="ba4" style="--h:46%"><div class="val" id="va4">0</div></div></div>
      <div class="col"><div class="fill b" id="bb4" style="--h:9%"><div class="val" id="vb4">0</div></div></div>
      <div class="gl">资本回报率</div></div>
  </div>
  <div class="note fx d3" id="k4c">毛利率只差 <b>13.64pct</b>，营业利润率差 <b>37.77pct</b>，资本回报率差 <b>36.83pct</b>——差距发生在毛利率以下。</div>
  <div class="foot fx d3" id="k5c">数据：2024 / 2025 年度报告（合并报表口径）</div>
</div>
""",
    "cues": [
        {"t": 200, "sel": "#k1c", "act": "on"},
        {"t": 450, "sel": "#k2c", "act": "on"},
        {"t": 700, "sel": "#k3c", "act": "on"},
        { "t": 900, "sel": "#chc", "act": "on" },
        { "t": 1250, "sel": "#bb1", "act": "on" },
        {"t": 1500, "sel": "#va1", "act": "count", "arg": 91.18, "dec": 2},
        {"t": 1600, "sel": "#vb1", "act": "count", "arg": 77.54, "dec": 2},
        { "t": 2400, "sel": "#ba2", "act": "on" },
        { "t": 2550, "sel": "#bb2", "act": "on" },
        {"t": 2800, "sel": "#va2", "act": "count", "arg": 68.00, "dec": 2},
        {"t": 2900, "sel": "#vb2", "act": "count", "arg": 30.23, "dec": 2},
        { "t": 3700, "sel": "#ba3", "act": "on" },
        { "t": 3850, "sel": "#bb3", "act": "on" },
        {"t": 4100, "sel": "#va3", "act": "count", "arg": 48.76, "dec": 2},
        {"t": 4200, "sel": "#vb3", "act": "count", "arg": 22.09, "dec": 2},
        { "t": 5000, "sel": "#ba4", "act": "on" },
        { "t": 5150, "sel": "#bb4", "act": "on" },
        {"t": 5400, "sel": "#va4", "act": "count", "arg": 46.29, "dec": 2},
        {"t": 5500, "sel": "#vb4", "act": "count", "arg": 9.46, "dec": 2},
        {"t": 6400, "sel": "#k4c", "act": "on"},
        {"t": 7200, "sel": "#k5c", "act": "on"},
    ],
    "dur": 22,
}

SHOTS = [S23, S31, S32, S33]
