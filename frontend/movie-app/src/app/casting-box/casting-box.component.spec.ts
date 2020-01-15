import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CastingBoxComponent } from './casting-box.component';

describe('CastingBoxComponent', () => {
  let component: CastingBoxComponent;
  let fixture: ComponentFixture<CastingBoxComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CastingBoxComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CastingBoxComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
