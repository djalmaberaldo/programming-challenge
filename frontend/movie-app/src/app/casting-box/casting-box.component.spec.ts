import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CastingBoxComponent } from './casting-box.component';
import { HttpClientModule } from '@angular/common/http';

describe('CastingBoxComponent', () => {
  let component: CastingBoxComponent;
  let fixture: ComponentFixture<CastingBoxComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientModule],
      declarations: [ CastingBoxComponent]
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
