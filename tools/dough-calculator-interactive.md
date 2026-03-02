---
layout: page
title: Water Temperature Calculator
permalink: /tools/desired-dough-temperature/
---

<!-- Interactive Dough Temperature Calculator -->

<section id="dough-calculator" class="calculator">

  <p class="calc-intro">Enter your temperatures below and the calculator will tell you what water temperature to use. Formula: <strong>Water Temp = (DDT × 3) − (Flour Temp + Room Temp + Friction Temp)</strong>.</p>

  <!-- ── INPUTS ─────────────────────────────────────── -->
  <div class="calc-section inputs-section">
    <h3 class="calc-section-heading">Inputs</h3>

    <div class="units-row">
      <label class="units-label">Units:
        <select id="unit">
          <option value="F">°F</option>
          <option value="C">°C</option>
        </select>
      </label>
    </div>

    <div class="grid">
      <label class="field">
        <span class="field-name">Desired Dough Temp <abbr title="Desired Dough Temperature">(DDT)</abbr></span>
        <input id="ddt" type="number" value="78" />
        <span class="field-hint">The final dough temperature you're aiming for</span>
      </label>

      <label class="field">
        <span class="field-name">Flour Temp</span>
        <input id="flour" type="number" value="75" />
        <span class="field-hint">Measure with a thermometer at the center of the bag</span>
      </label>

      <label class="field">
        <span class="field-name">Room Temp</span>
        <input id="room" type="number" value="72" />
        <span class="field-hint">Ambient temperature where you're mixing</span>
      </label>

      <label class="field">
        <span class="field-name">Friction Temp</span>
        <input id="friction" type="number" value="20" />
        <span class="field-hint">Heat from mixing — 0 for hand-mix, 10–25°F for a stand mixer</span>
      </label>

      <label class="field prefcheck" style="grid-column:1 / -1">
        <span class="field-name">Include pre-ferment?</span>
        <div class="checkbox-row">
          <input id="usePref" type="checkbox" />
          <span class="field-hint" style="margin-top:0">Check if your recipe uses a poolish, levain, or other pre-ferment</span>
        </div>
      </label>

      <div id="preWrap" style="display:none;grid-column:1 / -1;grid-template-columns:1fr 1fr;gap:0.75rem">
        <label class="field">
          <span class="field-name">Pre-ferment Temp</span>
          <input id="preTemp" type="number" value="75" />
          <span class="field-hint">Temperature of your starter or poolish</span>
        </label>
        <label class="field">
          <span class="field-name">Pre-ferment % of flour</span>
          <input id="prePercent" type="number" value="20" min="0" max="100" />
          <span class="field-hint">What % of total flour weight is in the pre-ferment</span>
        </label>
      </div>
    </div>
  </div>

  <!-- ── RESULT ─────────────────────────────────────── -->
  <div class="calc-section result-section">
    <h3 class="calc-section-heading">Result</h3>
    <div class="result-box">
      <span class="result-label">Target Water Temperature</span>
      <span id="water" class="result-value">—</span>
      <span class="result-hint">Add water at this temperature to hit your DDT</span>
    </div>
  </div>

  <p class="calc-notes">Results are advisory — always verify by experience. Friction values vary by mixer model and batch size.</p>

  <h3>Learn More</h3>
  <a href="https://www.kingarthurbaking.com/blog/2018/05/29/desired-dough-temperature" target="_blank">Why does dough temperature matter?</a>

<h3>Products that help</h3>


</section>

<style>
  .calculator {
    max-width: 680px;
    margin: 1rem 0;
    font-family: inherit;
  }

  .calc-intro {
    font-size: 0.95rem;
    color: #475569;
    margin-bottom: 1.5rem;
  }

  /* Sections */
  .calc-section {
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 1.25rem 1.25rem 1rem;
    margin-bottom: 1rem;
  }

  .inputs-section { background: #fafafa; }

  .calc-section-heading {
    font-size: 0.75rem !important;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #64748b;
    margin: 0 0 1rem 0 !important;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #e2e8f0;
  }

  /* Units row */
  .units-row {
    margin-bottom: 0.75rem;
  }

  .units-label {
    font-size: 0.9rem;
    font-weight: 600;
    color: #334155;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  /* Input grid */
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.75rem;
  }

  /* Individual fields */
  .field {
    display: flex;
    flex-direction: column;
    gap: 3px;
  }

  .field-name {
    font-size: 0.9rem;
    font-weight: 600;
    color: #334155;
  }

  .field input, .units-label select {
    padding: 0.45rem 0.6rem;
    border: 1px solid #cbd5e1;
    border-radius: 5px;
    font-size: 1rem;
    background: #fff;
    transition: border-color 0.15s;
  }

  .field input:focus, .units-label select:focus {
    outline: none;
    border-color: #8C6D46;
    box-shadow: 0 0 0 2px rgba(140,109,70,0.15);
  }

  .field-hint {
    font-size: 0.78rem;
    color: #94a3b8;
    margin-top: 2px;
    line-height: 1.3;
  }

  /* Pre-ferment checkbox row */
  .checkbox-row {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 2px;
  }

  .checkbox-row input[type="checkbox"] {
    width: 16px;
    height: 16px;
    flex-shrink: 0;
    accent-color: #8C6D46;
  }

  /* Result box */
  .result-section {
    background: #4A3728;
    border-color: #4A3728;
  }

  .result-section .calc-section-heading {
    color: rgba(255,255,255,0.6);
    border-bottom-color: rgba(255,255,255,0.15);
  }

  .result-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    padding: 0.5rem 0;
  }

  .result-label {
    font-size: 0.9rem;
    font-weight: 600;
    color: rgba(255,255,255,0.75);
  }

  .result-value {
    font-size: 2.5rem;
    font-weight: 700;
    color: #F7F4EF;
    letter-spacing: -0.02em;
    line-height: 1.1;
  }

  .result-hint {
    font-size: 0.8rem;
    color: rgba(255,255,255,0.5);
  }

  .calc-notes {
    font-size: 0.82rem;
    color: #94a3b8;
    margin-top: 0.5rem;
  }

  @media (max-width: 600px) {
    .grid { grid-template-columns: 1fr; }
    #preWrap { grid-template-columns: 1fr !important; }
    .result-value { font-size: 2rem; }
  }
</style>

<script>
  (function(){
    const $ = id => document.getElementById(id);
    const unit = $('unit');
    const inputs = ['ddt','flour','room','friction','preTemp'];
    const usePref = $('usePref');

    function parseVal(id){
      const v = parseFloat($(id).value);
      return Number.isFinite(v) ? v : 0;
    }

    function compute(){
      let ddt      = parseVal('ddt');
      let flour    = parseVal('flour');
      let room     = parseVal('room');
      let friction = parseVal('friction');

      let adjustedFlour = flour;
      if(usePref && usePref.checked){
        let preTemp    = parseVal('preTemp');
        let prePercent = parseFloat($('prePercent').value) || 0;
        let pf = Math.max(0, Math.min(100, prePercent)) / 100;
        adjustedFlour = (flour * (1 - pf)) + (preTemp * pf);
      }

      let water     = (ddt * 3) - (adjustedFlour + room + friction);
      const u       = unit.value;
      const rounded = Math.round(water * 10) / 10;

      const el = $('water');
      el.textContent = rounded + ' °' + u;

      const boiling = u === 'F' ? 212 : 100;
      if(rounded > boiling){
        el.style.color = '#f87171';
      } else if(rounded < (u === 'F' ? 32 : 0)){
        el.style.color = '#60a5fa';
      } else {
        el.style.color = '#F7F4EF';
      }
    }

    function toC(f){ return (f - 32) * (5/9); }
    function toF(c){ return (c * (9/5)) + 32; }

    function switchUnits(){
      const to = unit.value;
      inputs.forEach(id => {
        let v = parseVal(id);
        if(isNaN(v)) v = 0;
        $(id).value = to === 'C'
          ? Math.round(toC(v) * 10) / 10
          : Math.round(toF(v) * 10) / 10;
      });
      compute();
    }

    inputs.forEach(id => $(id).addEventListener('input', compute));
    if(usePref) $('prePercent').addEventListener('input', compute);
    if(usePref) usePref.addEventListener('change', function(){
      const wrap = $('preWrap');
      wrap.style.display = this.checked ? 'grid' : 'none';
      compute();
    });
    unit.addEventListener('change', switchUnits);

    compute();
  })();
</script>
