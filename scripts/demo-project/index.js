// Amethyst Hollow Theme — four shades of one violet
import { readFile } from 'node:fs/promises';

const CRYSTAL_SHADES = {
  deep: '#4C2365',
  mid: '#7F5D99',
  soft: '#9E7EB5',
  light: '#C4A4DA',
};

export class CrystalVein {
  constructor(name = 'Hollow seam') {
    this.name = name;
    this.shades = CRYSTAL_SHADES;
  }

  /** Blend two shades into a new facet colour. */
  blend(from, to, ratio = 0.5) {
    const parse = (hex) =>
      [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16));
    const [a, b] = [parse(from), parse(to)];
    const channel = (value, i) =>
      Math.round(value * (1 - ratio) + b[i] * ratio);
    const toHex = (value) => value.toString(16).padStart(2, '0');
    return '#' + a.map(channel).map(toHex).join('');
  }

  async readVein(file) {
    const content = await readFile(file, 'utf8');
    const seams = content.split('\n').filter(Boolean);
    return {
      name: this.name,
      shades: Object.keys(this.shades).length,
      seams: seams.length,
      content,
    };
  }
}

const vein = new CrystalVein();
const facet = vein.blend(CRYSTAL_SHADES.deep, CRYSTAL_SHADES.light);

console.log(`new facet: ${facet}`);
