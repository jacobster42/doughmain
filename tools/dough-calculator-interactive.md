---
layout: page
title: Dough Temperature Calculator (Interactive)
permalink: /tools/dough-calculator/
---

<!-- Interactive Dough Temperature Calculator -->

<section id="dough-calculator" class="calculator">
  <p>This calculator computes the target water temperature needed to reach a Desired Dough Temperature (DDT).
  Formula used: <strong>Water Temp = (DDT × 3) − (Flour Temp + Room Temp + Friction Temp)</strong>.</p>

  <label>Units:
    <select id="unit">
      <option value="F">°F</option>
      <option value="C">°C</option>
    </select>
  </label>

  <div class="grid">
    <label>Desired Dough Temp (DDT)
      <input id="ddt" type="number" value="78" />
    </label>

    <label>Flour Temp
      <input id="flour" type="number" value="75" />
    </label>

    <label>Room Temp
      <input id="room" type="number" value="72" />
    </label>

    <label>Friction Temp
      <input id="friction" type="number" value="20" />
    </label>

    <label style="grid-column:1 / -1">Include pre-ferment
      <div style="display:flex;gap:0.5rem;align-items:center">
        <input id="usePref" type="checkbox" />
        <small>Show pre-ferment inputs</small>
      </div>
    </label>

    <div id="preWrap" style="display:none;grid-column:1 / -1;display:grid;grid-template-columns:1fr 1fr;gap:0.5rem">
      <label>Pre-ferment Temp
        <input id="preTemp" type="number" value="75" />
      </label>
      <label>Pre-ferment % of flour
        <input id="prePercent" type="number" value="20" min="0" max="100" />
      </label>
    </div>

    <label>Water Temp (result)
      <input id="water" type="text" readonly />
    </label>
  </div>

  <div class="notes">
    <p><strong>Notes:</strong> Friction temp depends on your mixer and mixing time — common values: 0 (hand-mix), 10–25°F (mixer). Adjust for °C if needed. Results are advisory; always validate by experience.</p>
  </div>
</section>

<style>
  .calculator{max-width:720px;margin:1rem 0;padding:1rem;border:1px solid #e2e8f0;border-radius:6px}
  .calculator .grid{display:grid;grid-template-columns:1fr 1fr;gap:0.5rem}
  .calculator label{display:flex;flex-direction:column;font-size:0.95rem}
  .calculator input, .calculator select{padding:0.35rem;border:1px solid #cbd5e1;border-radius:4px}
  .calculator input[readonly]{background:#f8fafc}
  .calculator .notes{margin-top:0.8rem;font-size:0.9rem;color:#475569}
  @media(max-width:600px){.calculator .grid{grid-template-columns:1fr}}
</style>

<script>
  (function(){
    const $ = id => document.getElementById(id);
    const unit = $('unit');
    const inputs = ['ddt','flour','room','friction','preTemp'];
    const usePref = $('usePref');

    function parseVal(id){
      const v = parseFloat($(id).value);
      return Number.isFinite(v)? v : 0;
    }

    function compute(){
      // read values
      let ddt = parseVal('ddt');
      let flour = parseVal('flour');
      let room = parseVal('room');
      let friction = parseVal('friction');

      // handle optional pre-ferment by adjusting flour temp as weighted average
      let adjustedFlour = flour;
      if(usePref && usePref.checked){
        let preTemp = parseVal('preTemp');
        let prePercent = parseFloat($('prePercent').value) || 0;
        let pf = Math.max(0, Math.min(100, prePercent)) / 100;
        adjustedFlour = (flour * (1 - pf)) + (preTemp * pf);
      }

      // formula: water = (DDT * 3) - (adjustedFlour + room + friction)
      let water = (ddt * 3) - (adjustedFlour + room + friction);

      const u = unit.value;
      const formatted = Math.round(water*10)/10;
      $('water').value = formatted + ' °' + u;

      // if using pre-ferment, show adjusted flour temp in the field title for clarity
      if(usePref && usePref.checked){
        $('water').title = 'Adjusted flour temp: ' + (Math.round(adjustedFlour*10)/10) + ' °' + u + ( $('water').title? ' — ' + $('water').title : '');
      }

      // add warnings as title
      let msg = '';
      if(u==='F' && formatted > 212) msg = 'Result exceeds boiling point; check inputs.';
      if(u==='C' && formatted > 100) msg = 'Result exceeds boiling point; check inputs.';
      $('water').title = msg;
    }

    // conversion helpers when units change
    function toC(f){return (f - 32) * (5/9)}
    function toF(c){return (c * (9/5)) + 32}

    function switchUnits(){
      const to = unit.value;
      // convert all numeric inputs to selected unit
      inputs.forEach(id=>{
        let v = parseVal(id);
        if(isNaN(v)) v = 0;
        if(to==='C') v = Math.round(toC(v)*10)/10;
        else v = Math.round(toF(v)*10)/10;
        $(id).value = v;
      });
      compute();
    }

    // attach listeners
    inputs.forEach(id=>$(id).addEventListener('input', compute));
    if(usePref) $('prePercent').addEventListener('input', compute);
    if(usePref) usePref.addEventListener('change', function(){
      const wrap = $('preWrap');
      if(this.checked) wrap.style.display = 'grid'; else wrap.style.display = 'none';
      compute();
    });
    unit.addEventListener('change', switchUnits);

    // initial compute
    compute();
  })();
</script>
