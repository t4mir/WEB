import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GamesallComponent } from './gamesall.component';

describe('GamesallComponent', () => {
  let component: GamesallComponent;
  let fixture: ComponentFixture<GamesallComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GamesallComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GamesallComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
