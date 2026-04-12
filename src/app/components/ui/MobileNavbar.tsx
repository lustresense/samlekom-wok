import { useState, useEffect } from 'react';
import { Home, Calendar, User as UserIcon, Menu, X, LogOut, BadgeCheck } from 'lucide-react';
import { motion, AnimatePresence } from 'motion/react';
import { Button } from '@/app/components/ui/button';
import { Badge } from '@/app/components/ui/badge';

interface MobileNavbarProps {
  user: any;
  activePage: string;
  onLogout: () => void;
  onNavigate: (page: any) => void;
  userMode: 'relawan' | 'ksh';
  onModeChange: (mode: 'relawan' | 'ksh') => void;
  currentView: 'admin' | 'moderator' | 'user';
  onViewChange: (view: 'admin' | 'moderator' | 'user') => void;
  moderatorTier: 1 | 2 | 3;
  onModeratorTierChange: (tier: 1 | 2 | 3) => void;
  theme?: 'user' | 'moderator';
  navItems?: Array<{ key: string; label: string; icon: any }>;
}

const SPRING = { type: 'spring' as const, stiffness: 250, damping: 25 };
const FADE_TRANSITION = { duration: 0.1 };

export function MobileNavbar({
  user,
  activePage,
  onLogout,
  onNavigate,
  userMode,
  onModeChange,
  currentView,
  onViewChange,
  moderatorTier,
  onModeratorTierChange,
  theme = 'user',
  navItems,
}: MobileNavbarProps) {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isOpen, setIsOpen] = useState(false);
  const isModerator = theme === 'moderator';

  const palette = isModerator
    ? {
        border: 'border-cyan-200',
        active: 'bg-cyan-600 text-white',
        inactive: 'text-cyan-900 hover:bg-cyan-50',
        menu: 'bg-cyan-700 hover:bg-cyan-800',
        ksh: 'bg-cyan-200 text-cyan-900',
      }
    : {
        border: 'border-green-200',
        active: 'bg-green-600 text-white',
        inactive: 'text-green-800 hover:bg-green-50',
        menu: 'bg-green-700 hover:bg-green-800',
        ksh: 'bg-yellow-400 text-black',
      };

  const items = navItems || [
    { key: 'home', label: 'Home', icon: Home },
    { key: 'events', label: 'Event', icon: Calendar },
    { key: 'profile', label: 'Profil', icon: UserIcon },
  ];

  useEffect(() => {
    const handleScroll = () => setIsScrolled(window.scrollY > 20);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <div className="fixed top-3 left-0 right-0 z-50">
      <div className="mx-auto flex justify-center px-4">
        <AnimatePresence mode="wait">
          {/* ==================== CLOSED PILL (mobile) ==================== */}
          {!isOpen ? (
            <motion.div
              key="mobile-pill"
              layoutId="mobile-nav-container"
              transition={SPRING}
              onClick={() => setIsOpen(true)}
              className={`flex cursor-pointer items-center gap-1 rounded-full border bg-white/95 px-3 py-2 shadow-lg backdrop-blur ${
                isScrolled ? 'shadow-xl' : ''
              } ${palette.border}`}
            >
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0, transition: FADE_TRANSITION }}
                className="flex items-center"
              >
                {/* Nav items — labels hidden on mobile */}
                {items.map((item) => {
                  const Icon = item.icon;
                  const isActive = activePage === item.key;
                  return (
                    <button
                      key={item.key}
                      onClick={(e) => {
                        e.stopPropagation();
                        onNavigate(item.key);
                      }}
                      className={`flex items-center justify-center rounded-full p-2 text-sm font-semibold transition ${
                        isActive ? palette.active : palette.inactive
                      }`}
                    >
                      <Icon className="h-5 w-5" />
                    </button>
                  );
                })}

                {/* Menu toggle */}
                <div
                  onClick={(e) => {
                    e.stopPropagation();
                    setIsOpen(true);
                  }}
                  className={`ml-1 flex h-10 w-10 cursor-pointer items-center justify-center rounded-full text-white shadow transition ${palette.menu}`}
                >
                  <Menu className="h-4 w-4" />
                </div>
              </motion.div>
            </motion.div>
          ) : (
            /* ==================== OPEN MODAL (mobile) ==================== */
            <motion.div
              key="mobile-modal"
              layoutId="mobile-nav-container"
              transition={SPRING}
              className={`w-80 max-w-[90vw] rounded-2xl border bg-white/95 shadow-xl backdrop-blur ${palette.border}`}
            >
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0, transition: FADE_TRANSITION }}
                transition={FADE_TRANSITION}
              >
                {/* User Header */}
                <div className="flex items-center justify-between border-b border-gray-100 p-4">
                  <div className="flex items-center gap-3">
                    <div
                      className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-full font-bold text-white ${
                        isModerator ? 'bg-cyan-700' : 'bg-green-700'
                      }`}
                    >
                      {user?.name?.charAt(0) || 'U'}
                    </div>
                    <div className="min-w-0">
                      <p className="truncate text-sm font-bold text-gray-900">{user?.name}</p>
                      <div className="flex items-center gap-1 text-xs text-gray-500">
                        <span>{user?.role}</span>
                        {userMode === 'ksh' && (
                          <Badge className={`${palette.ksh} shrink-0 px-1.5 py-0 text-[9px]`}>
                            <BadgeCheck className="mr-0.5 h-2.5 w-2.5" />
                            KSH
                          </Badge>
                        )}
                      </div>
                    </div>
                  </div>
                  <button
                    onClick={() => setIsOpen(false)}
                    className={`shrink-0 rounded-full p-1.5 text-white transition ${palette.menu}`}
                  >
                    <X className="h-4 w-4" />
                  </button>
                </div>

                {/* Admin POV Controls */}
                {user?.role === 'admin' && (
                  <div className="space-y-3 border-b border-gray-100 px-4 py-3">
                    <div>
                      <p className="mb-1.5 text-[10px] font-semibold uppercase text-gray-400">Kategori</p>
                      <div className="grid grid-cols-2 gap-1.5">
                        <Button
                          size="sm"
                          variant={currentView === 'user' && userMode === 'relawan' ? 'default' : 'outline'}
                          onClick={(e) => {
                            e.stopPropagation();
                            onModeChange('relawan');
                            onViewChange('user');
                          }}
                          className={`h-7 text-xs ${
                            currentView === 'user' && userMode === 'relawan'
                              ? isModerator
                                ? 'bg-cyan-600 text-white'
                                : 'bg-green-600 text-white'
                              : ''
                          }`}
                        >
                          Relawan
                        </Button>
                        <Button
                          size="sm"
                          variant={currentView === 'user' && userMode === 'ksh' ? 'default' : 'outline'}
                          onClick={(e) => {
                            e.stopPropagation();
                            onModeChange('ksh');
                            onViewChange('user');
                          }}
                          className={`h-7 text-xs ${
                            currentView === 'user' && userMode === 'ksh'
                              ? isModerator
                                ? 'bg-cyan-200 text-cyan-900'
                                : 'bg-yellow-400 text-black'
                              : ''
                          }`}
                        >
                          KSH
                        </Button>
                      </div>
                    </div>

                    <div>
                      <p className="mb-1.5 text-[10px] font-semibold uppercase text-gray-400">Mod Tier</p>
                      <div className="grid grid-cols-3 gap-1.5">
                        {([1, 2, 3] as const).map((tier) => (
                          <Button
                            key={tier}
                            size="sm"
                            variant={currentView === 'moderator' && moderatorTier === tier ? 'default' : 'outline'}
                            onClick={(e) => {
                              e.stopPropagation();
                              onModeratorTierChange(tier);
                              onViewChange('moderator');
                            }}
                            className={`h-7 text-xs ${
                              currentView === 'moderator' && moderatorTier === tier
                                ? 'bg-cyan-600 text-white'
                                : ''
                            }`}
                          >
                            Tier {tier}
                          </Button>
                        ))}
                      </div>
                    </div>

                    <div>
                      <p className="mb-1.5 text-[10px] font-semibold uppercase text-gray-400">View</p>
                      <div className="grid grid-cols-2 gap-1.5">
                        <Button
                          size="sm"
                          variant={currentView === 'user' ? 'default' : 'outline'}
                          onClick={(e) => {
                            e.stopPropagation();
                            onViewChange('user');
                          }}
                          className={`h-7 text-xs ${
                            currentView === 'user'
                              ? isModerator
                                ? 'bg-cyan-700 text-white'
                                : 'bg-green-700 text-white'
                              : ''
                          }`}
                        >
                          User
                        </Button>
                        <Button
                          size="sm"
                          variant={currentView === 'admin' ? 'default' : 'outline'}
                          onClick={(e) => {
                            e.stopPropagation();
                            onViewChange('admin');
                          }}
                          className={`h-7 text-xs ${currentView === 'admin' ? 'bg-black text-white' : ''}`}
                        >
                          Admin
                        </Button>
                      </div>
                    </div>
                  </div>
                )}

                {/* Nav Links */}
                <div className="space-y-0.5 p-2">
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      onNavigate('profile');
                      setIsOpen(false);
                    }}
                    className="flex w-full items-center gap-3 rounded-xl px-3 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50"
                  >
                    <UserIcon className="h-4 w-4 shrink-0" />
                    Profil Saya
                  </button>
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      onLogout();
                      setIsOpen(false);
                    }}
                    className="flex w-full items-center gap-3 rounded-xl px-3 py-2.5 text-sm font-medium text-red-600 hover:bg-red-50"
                  >
                    <LogOut className="h-4 w-4 shrink-0" />
                    Keluar
                  </button>
                </div>
              </motion.div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}
