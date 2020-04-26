import { TestBed } from '@angular/core/testing';

import { AuthentifyService } from './authentify.service';

describe('AuthentifyService', () => {
  let service: AuthentifyService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AuthentifyService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
