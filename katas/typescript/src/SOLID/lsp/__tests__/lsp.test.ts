/**
 * Tests para el Liskov Substitution Principle (LSP)
 * Valida tanto las implementaciones malas como las buenas
 */

import { Rectangle as RectangleBad, Square as SquareBad } from "../lsp-bad";
import { Rectangle as RectangleGood, Square as SquareGood } from "../lsp-good";

describe("LSP - Bad Implementation", () => {
  test("should calculate rectangle area correctly", () => {
    const rect = new RectangleBad(5, 10);
    expect(rect.calculateArea()).toBe(50);
  });

  test("should calculate square area correctly", () => {
    const square = new SquareBad(5);
    expect(square.calculateArea()).toBe(25);
  });

  test("demonstrates LSP violation with square", () => {
    const rect: RectangleBad = new SquareBad(5);
    rect.setWidth(10);
    rect.setHeight(5);
    // Square violates LSP: setting width also sets height
    expect(rect.calculateArea()).not.toBe(50); // Should be 50, but it's 25
  });
});

describe("LSP - Good Implementation", () => {
  test("should calculate rectangle area correctly", () => {
    const rect = new RectangleGood(5, 10);
    expect(rect.calculateArea()).toBe(50);
  });

  test("should calculate square area correctly", () => {
    const square = new SquareGood(5);
    expect(square.calculateArea()).toBe(25);
  });

  test("should maintain rectangle dimensions independently", () => {
    const rect = new RectangleGood(5, 10);
    rect.setWidth(8);
    rect.setHeight(6);
    expect(rect.calculateArea()).toBe(48);
  });

  test("should maintain square dimensions together", () => {
    const square = new SquareGood(5);
    square.setSide(7);
    expect(square.calculateArea()).toBe(49);
  });

  test("demonstrates LSP compliance - separate hierarchies", () => {
    // Rectangle and Square are no longer in inheritance relationship
    // Each has its own appropriate interface
    const rect = new RectangleGood(10, 5);
    const square = new SquareGood(5);

    expect(rect.calculateArea()).toBe(50);
    expect(square.calculateArea()).toBe(25);
  });
});
