import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ToptenhotComponent } from './toptenhot.component';

describe('ToptenhotComponent', () => {
  let component: ToptenhotComponent;
  let fixture: ComponentFixture<ToptenhotComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ToptenhotComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ToptenhotComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
