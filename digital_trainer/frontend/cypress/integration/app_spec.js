describe("Django REST framework / React quickstart app", () => {
  const movement = {
    name: "Armin",
    description: "some-email@gmail.com",
    video: "http://IamlookingforaReacttutor.com",
    unilateral: "False",
    difficulty: "ADV"
  };
  before(() => {
    cy.exec("npm run dev");
    cy.exec("npm run flush");
  });
  it("should be able to fill a web form", () => {
    cy.visit("/");
    cy
      .get('input[name="name"]')
      .type(movement.name)
      .should("have.value", movement.name);
    cy
      .get('input[name="description"]')
      .type(movement.description)
      .should("have.value", movement.description);
    cy
      .get('input[name="video"]')
      .type(movement.video)
      .should("have.value", movement.video);
    cy
      .get('input[name="difficulty"]')
      .type(movement.difficulty)
      .should("have.value", movement.difficulty);
    cy.get("form").submit();
  });
  // more tests here
});
